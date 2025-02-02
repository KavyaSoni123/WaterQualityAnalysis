import pandas as pd
import ee
from datetime import timedelta
import datetime
from datetime import timedelta


ee.Initialize(project="ee-sujalrajput10")
file_path = "C:/Users/sujal/OneDrive/Desktop/Projects/Sattelite_data/Adding_data/WaterQualityAnalysis/data/FInal_dataset/Lake_erie_final.csv"

# Read CSV Data

df = pd.read_csv(file_path)
df["Date"] = pd.to_datetime(df["Date"])

# df = pd.read_csv('/content/GLORIA_WesternErie.csv')

# df['Date_Time_UTC'] = pd.to_datetime(df['Date_Time_UTC'])
# # Create separate columns for Date and Time
# df["Date"] = df["Date_Time_UTC"].dt.date
# df["Time"] = df["Date_Time_UTC"].dt.time
# df['Date'] = pd.to_datetime(df['Date'])


# Function to extract coordinates for a specific date
def extract_coor(date):
    # Filter the dataframe where the date matches
    filtered_data = df[df["Date"].dt.date == date][["Longitude", "Latitude"]]
    # Convert the filtered data to a list of tuples
    coordinates = list(filtered_data.itertuples(index=False, name=None))
    return coordinates


# Extract unique dates (only the date part)
dates = df["Date"].dt.date.unique()  # This gives `date` objects, not `datetime`


# Loop through unique dates and call the function
cooridinates = []
for date in dates:
    cooridinates.append(extract_coor(date))


# Define the Area of Interest (AOI)
AOI = ee.Geometry.Polygon([[-83.5, 41.6], [-83.5, 41.7], [-83.3, 41.7], [-83.3, 41.6]])


def data_extract_df(AOI, coordinates, date, cloud_threshold=20, days=3):
    """
    Extract Sentinel-2 satellite data for a given Area of Interest (AOI) and coordinates.

    Args:
        AOI: ee.Geometry object defining the Area of Interest.
        coordinates: List of tuples representing latitude and longitude points.
        date: datetime object representing the target date.
        cloud_threshold: Maximum allowable cloud cover percentage. Default is 20.
        days: Range of days around the target date for data extraction. Default is 3.

    Returns:
        pd.DataFrame: A DataFrame containing the extracted satellite data for the given coordinates.
    """
    print(date)
    try:
        # Validate input arguments
        if not AOI:
            raise ValueError("Area of Interest (AOI) is missing.")
        if not coordinates:
            raise ValueError("Coordinates list is empty.")

        # Create date range
        start_date = (date - timedelta(days)).strftime("%Y-%m-%d")
        end_date = (date + timedelta(days)).strftime("%Y-%m-%d")
        print(f"Date range for data extraction: {start_date} to {end_date}")

        # Cloud masking function
        def maskS2clouds(image):
            qa = image.select("QA60")
            cloudBitMask = 1 << 10
            cirrusBitMask = 1 << 11
            mask = (
                qa.bitwiseAnd(cloudBitMask)
                .eq(0)
                .And(qa.bitwiseAnd(cirrusBitMask).eq(0))
            )
            return image.updateMask(mask).divide(10000)  # Normalize reflectance values

        # Define the Sentinel-2 ImageCollection
        S2 = (
            ee.ImageCollection("COPERNICUS/S2_SR_HARMONIZED")
            .filterDate(start_date, end_date)
            .filter(ee.Filter.lt("CLOUDY_PIXEL_PERCENTAGE", cloud_threshold))
            .map(maskS2clouds)
            .filterBounds(AOI)
        )

        # Count the number of images in the collection
        image_count = S2.size().getInfo()
        print(f"Number of images found: {image_count}")

        if image_count == 0:
            print(
                "\033[91mNo data found in the specified time range.\033[0m \n"
            )  # Red text for no data
            return pd.DataFrame()  # Return an empty DataFrame if no data found

        # Select specific bands for analysis
        selectedBands = S2.select(
            ["B2", "B3", "B4", "B5", "B6", "B7", "B8", "B8A", "B11", "B12"]
        )
        print(
            "Bands selected for analysis: ['B2', 'B3', 'B4', 'B5', 'B6', 'B7', 'B8', 'B8A', 'B11', 'B12']"
        )

        # Reduce the ImageCollection to the median value
        medianImage = selectedBands.median()

        # Create FeatureCollection from coordinates
        samplePoints = ee.FeatureCollection(
            [ee.Feature(ee.Geometry.Point([lon, lat])) for lon, lat in coordinates]
        ).map(
            lambda feature: feature.set(
                {
                    "Latitude": feature.geometry().coordinates().get(1),
                    "Longitude": feature.geometry().coordinates().get(0),
                }
            )
        )

        print(f"Number of sample points: {len(coordinates)}")

        # Extract data at sample points
        sampledData = medianImage.sampleRegions(
            collection=samplePoints,
            scale=10,  # Sentinel-2 resolution in meters
            geometries=True,
        )

        # Check for empty samples
        sample_count = sampledData.size().getInfo()
        if sample_count == 0:
            print(
                "\033[91mNo samples found in the specified time range.\033[0m \n"
            )  # Red text for no samples
            return pd.DataFrame()  # Return an empty DataFrame if no samples found
        else:
            print(
                "\033[92mSamples extracted successfully.\033[0m"
            )  # Green text for successful extraction

        # Convert sampled data to a list of dictionaries
        sampled_dict = sampledData.getInfo()
        features = sampled_dict["features"]
        rows = []
        for feature in features:
            row = feature["properties"]
            row["Date"] = date.strftime("%Y-%m-%d")
            row["Latitude"] = feature["geometry"]["coordinates"][1]
            row["Longitude"] = feature["geometry"]["coordinates"][0]
            rows.append(row)

        # Create a DataFrame from the extracted data
        df = pd.DataFrame(rows)
        print("Data extraction completed and converted to DataFrame.\n")

        return df

    except ValueError as ve:
        print(f"ValueError: {ve}")
        return pd.DataFrame()  # Return an empty DataFrame in case of error

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


final_df = pd.DataFrame()
for i in range(len(cooridinates)):
    final_df = pd.concat(
        [final_df, data_extract_df(AOI, cooridinates[i], dates[i])], ignore_index=True
    )


# Ensure the columns have the same data types
df["Date"] = pd.to_datetime(df["Date"])
final_df["Date"] = pd.to_datetime(final_df["Date"])
df["Latitude"] = df["Latitude"].astype(float)
final_df["Latitude"] = final_df["Latitude"].astype(float)
df["Longitude"] = df["Longitude"].astype(float)
final_df["Longitude"] = final_df["Longitude"].astype(float)

# Round Latitude and Longitude in both dataframes to 4 decimal places
df["Latitude"] = df["Latitude"].round(4)
df["Longitude"] = df["Longitude"].round(4)

final_df["Latitude"] = final_df["Latitude"].round(4)
final_df["Longitude"] = final_df["Longitude"].round(4)

merged_df = pd.merge(df, final_df, on=["Date", "Latitude", "Longitude"], how="inner")


prefix = "custom_merged_data"
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
custom_filename = f"C:/Users/sujal/OneDrive/Desktop/Projects/Sattelite_data/Adding_data/WaterQualityAnalysis/data/{prefix}_{timestamp}.csv"

# Save the DataFrame to CSV with custom filename
merged_df.to_csv(custom_filename, index=False)
