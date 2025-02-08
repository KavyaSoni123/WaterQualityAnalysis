import pandas as pd
import ee
from datetime import timedelta
import datetime


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
    print(f"Extracting data for date: {date.strftime('%Y-%m-%d')}")
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
