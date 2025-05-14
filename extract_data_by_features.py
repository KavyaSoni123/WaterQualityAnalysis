import pandas as pd
from cleaner import process_and_save_top_clusters

"""
example use case
by default we take top five lakes
process_and_save_top_clusters(df, "DOC", num_clusters=3)  # Example with 3 clusters
"""


# List of water quality features to process
features = ["Chl-a", "TURB", "TSS", "DOC", "TP", "TN", "O2-Dis", "EC", "TDS"]

# Load dataset
df = pd.read_csv("data/Gemstat_Data_Cleaned_Raw/All_lakes_clustered_haversine.csv")
df["Date"] = pd.to_datetime(df["Date"], errors="coerce")

# Filter data after 2018
df_after_2018 = df[df["Date"] > "2017-12-31"]

# Process and save top clusters for each feature
for feature in features:
    process_and_save_top_clusters(
        df_after_2018, featurebase_path="data/Gemstat_Data_Cleaned_2018"
    )

print("Processing complete for all features.")
