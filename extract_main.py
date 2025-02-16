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


DATA_AOI_DICT = {
#     # AOI for Lake Baikal
#     "Lake_baikal": ee.Geometry.Polygon(
#         [
#             [102.71284237056808, 50.95014919458215],
#             [111.61176815181808, 50.95014919458215],
#             [111.61176815181808, 55.991032052704064],
#             [102.71284237056808, 55.991032052704064],
#             [102.71284237056808, 50.95014919458215],
#         ]
#     ),
#     "Cluster_393": ee.Geometry.Polygon([
#             [-101.55215959467778,19.691358874646745],
#             [-101.6527531615723,19.6923286088422],
#             [-101.7348072997559,19.561037952791715],
#             [-101.60022478022465,19.514446076076492],
#             [-101.53087358393559,19.665820427626194],
#             [-101.55215959467778,19.691358874646745],
#     ]),
#     "Cluster_455": ee.Geometry.Polygon(
#         [
#     [-98.34343540697125, 22.591849098310146],
#     [-98.59062778978375, 22.08884615164201],
#     [-98.17177403001813, 21.95771852669186],
#     [-98.05092442064313, 21.914407065701592],
#     [-97.97951328783063, 21.934790572152636],
#     [-97.83669102220563, 22.060848509011578],
#     [-97.802358746815, 22.18679414928777],
#     [-97.93007481126813, 22.45103913243088],
#     [-98.34343540697125, 22.591849098310146]
# ]

#     ),
#     "Cluster_539": ee.Geometry.Polygon(
#         [
#     [-93.88620754842876, 18.21071462774072],
#     [-93.76604458456157, 18.183317809262878],
#     [-93.52640530233501, 18.294835031439085],
#     [-93.45911404256938, 18.401719854605876],
#     [-93.53052517538188, 18.40758356927238],
#     [-93.68570706014751, 18.35806148470228],
#     [-93.89170071249126, 18.287011596811897],
#     [-93.88620754842876, 18.21071462774072]
# ]

#     ),
#     "Cluster_616": ee.Geometry.Polygon(
#         [
#     [-97.52937269501423, 15.999594641869288],
#     [-97.6371760397408, 16.036883835538557],
#     [-97.66841841034626, 16.011805144924413],
#     [-97.76660871796345, 16.007515053238137],
#     [-97.77690840058064, 15.984082926950926],
#     [-97.69416761688923, 15.965269233067923],
#     [-97.63992262177204, 15.982102621412297],
#     [-97.55924177460408, 15.964609071349669],
#     [-97.5115199118111, 15.9705504484677],
#     [-97.52937269501423, 15.999594641869288]
# ]

#     ),
#     "Cluster_626": ee.Geometry.Polygon(
#         [
#     [-86.84774351410603, 21.235682150118695],
#     [-86.81100797943806, 21.183991387616842],
#     [-86.80877638153767, 21.19503520650964],
#     [-86.80740309052204, 21.214399910351027],
#     [-86.80482816986775, 21.24368219788763],
#     [-86.8130679159615, 21.25024191304796],
#     [-86.82834577851033, 21.239202224624638],
#     [-86.84190702728962, 21.24256221733709],
#     [-86.84774351410603, 21.235682150118695]
# ]

    # ),
    "India": ee.Geometry.Polygon(
        [
    [75.77565271921756, 6.9864704398759],
    [80.52174646921756, 9.94186146304483],
    [80.17018396921756, 15.172941183159757],
    [87.37721521921756, 21.59110251939127],
    [93.00221521921756, 21.672803090419787],
    [96.42994959421756, 28.666547402405033],
    [89.66237146921756, 27.191185389662316],
    [88.34401209421756, 28.4349398141589],
    [87.55299646921756, 26.878037974445018],
    [80.52174646921756, 28.820668884226627],
    [80.87330896921756, 31.480263469366818],
    [80.17018396921756, 36.71692205432753],
    [72.08424646921756, 37.278474844923856],
    [70.94166834421756, 30.425048229557017],
    [68.12916834421756, 23.377614968760405],
    [75.77565271921756, 6.9864704398759]
]
    ),
    
    # add more lakes here(no chat gpt for AOI)
}

# timeframes = [1, 3, 5, 7, 14]
timeframes = [1,7]


# Lake erie coordinate(kept for tesing purposes)
# AOI = ee.Geometry.Polygon([[-83.5, 41.6], [-83.5, 41.7], [-83.3, 41.7], [-83.3, 41.6]])
# dataset_name = "Lake_erie_final"


def main(AOI, dataset_name, timeframe, subfolder, name):
    # file_path = f"{DATASET_FILE_PATH}{dataset_name}.csv"
    file_path = "data/temp/TotalColiIndia.csv"
    df = pd.read_csv(file_path)
    df["Date"] = pd.to_datetime(df["Date"])

    dates = extract_dates(df)
    cooridinates = []
    for date in dates:
        cooridinates.append(extract_coor(date, df))

    final_df = pd.DataFrame()
    for i in range(len(cooridinates)):
        print(f"\nCurrent dataset is {dataset_name}")
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

    # output_dir = os.path.join(f"{OUTPUT_FOLDER}", subfolder)
    output_dir = "data/temp/"
    os.makedirs(output_dir, exist_ok=True)

    # Define the custom filename
    custom_filename = os.path.join(output_dir, f"{name}.csv")

    # Save the DataFrame to CSV
    merged_df.to_csv(custom_filename, index=False)


if __name__ == "__main__":
    for dataset_name, AOI in DATA_AOI_DICT.items():
        subfolder = dataset_name  # Create a folder per dataset

        for time in timeframes:
            print(
                Fore.CYAN
                + f"⏳ Processing {dataset_name} for {time}-day time span... ⏳"
                + Style.RESET_ALL
            )
            print("\n" * 2)

            name = f"{dataset_name}_{time}_days"

            main(AOI, dataset_name, time, subfolder, name)

            print("\n" * 2)
            print(
                Fore.GREEN
                + f"✅ Completed {dataset_name} for {time}-day time span! ✅"
                + Style.RESET_ALL
            )
            print("\n" * 2)
