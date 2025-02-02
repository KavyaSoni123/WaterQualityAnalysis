from extract import extract_dates, extract_coor, data_extract_df
import pandas as pd
import ee


# Initialize Earth Engine and define the path to the CSV file
ee.Initialize(project="ee-sujalrajput10")
file_path = "C:/Users/sujal/OneDrive/Desktop/Projects/Sattelite_data/Adding_data/WaterQualityAnalysis/data/FInal_dataset/Lake_erie_final.csv"
AOI = ee.Geometry.Polygon([[-83.5, 41.6], [-83.5, 41.7], [-83.3, 41.7], [-83.3, 41.6]])
timeframe = 3
subfolder = "temp"
name = "extr_data"


df = pd.read_csv(file_path)
df["Date"] = pd.to_datetime(df["Date"])


dates = extract_dates(df)
cooridinates = []
for date in dates:
    cooridinates.append(extract_coor(date, df))

final_df = pd.DataFrame()
for i in range(len(cooridinates)):
    final_df = pd.concat(
        [final_df, data_extract_df(AOI, cooridinates[i], dates[i], days=timeframe)],
        ignore_index=True,
    )

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


custom_filename = f"C:/Users/sujal/OneDrive/Desktop/Projects/Sattelite_data/Adding_data/WaterQualityAnalysis/data/{subfolder}/{name}.csv"

# Save the DataFrame to CSV with custom filename
merged_df.to_csv(custom_filename, index=False)
