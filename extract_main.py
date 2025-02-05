import ee
import pandas as pd
import os
from extract import extract_dates, extract_coor, data_extract_df
from config import DATASET_FILE_PATH, OUTPUT_FOLDER, PROJECT_ID
from colorama import Fore, Style, init

init(autoreset=True)

try:
    ee.Initialize(project=PROJECT_ID)
    print(Fore.BLUE + "🌍 Earth Engine initialized successfully! 🌍" + Style.RESET_ALL)
    print("\n" * 2)
except Exception as e:
    print("Error initializing Earth Engine:", e)


AOI = ee.Geometry.Polygon([[-83.5, 41.6], [-83.5, 41.7], [-83.3, 41.7], [-83.3, 41.6]])
timeframes = [3, 5, 7, 14]
dataset_name = "Lake_erie_final"


def main(AOI, dataset_name, timeframe, subfolder, name):
    file_path = f"{DATASET_FILE_PATH}{dataset_name}.csv"
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

    merged_df = pd.merge(
        df, final_df, on=["Date", "Latitude", "Longitude"], how="inner"
    )

    output_dir = os.path.join(f"{OUTPUT_FOLDER}", subfolder)
    os.makedirs(output_dir, exist_ok=True)

    # Define the custom filename
    custom_filename = os.path.join(output_dir, f"{name}.csv")

    # Save the DataFrame to CSV
    merged_df.to_csv(custom_filename, index=False)


if __name__ == "__main__":
    subfolder = dataset_name

    for time in timeframes:
        # Starting message with emojis and text
        print(
            Fore.CYAN
            + f"⏳ Starting to create dataset for {time}-day time span... ⏳"
            + Style.RESET_ALL
        )
        print("\n" * 2)  # Adding some space

        name = f"{time}_days"
        main(AOI, dataset_name, time, subfolder, name)

        # Ending message with emojis and text
        print("\n" * 2)  # Adding space before the end message
        print(
            Fore.GREEN
            + f"✅ Data creation complete for {time}-day time span! ✅"
            + Style.RESET_ALL
        )
        print("\n" * 2)  # Adding space after the end message
