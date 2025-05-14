import os


def process_and_save_top_clusters(
    df, feature_col, num_clusters=5, base_path="data/Gemstat_Data_Cleaned"
):
    """
    Processes and saves the top clusters for a given feature.

    Parameters:
    - df: Pandas DataFrame containing the dataset.
    - feature_col: The feature for which clusters need to be analyzed and saved.
    - num_clusters: Number of top clusters to save.
    - base_path: Base directory where the datasets will be stored.
    """
    # Step 1: Compute top clusters based on feature count
    cluster_counts = (
        df.dropna(subset=[feature_col])
        .groupby("Cluster")[feature_col]
        .count()
        .reset_index()
        .rename(columns={feature_col: f"{feature_col}_count"})
        .sort_values(by=f"{feature_col}_count", ascending=False)
        .head(num_clusters)  # Select top clusters
    )

    # Step 2: Create a subfolder based on the feature name
    feature_folder = os.path.join(base_path, feature_col.replace(" ", "_"))
    os.makedirs(feature_folder, exist_ok=True)

    # Step 3: Save filtered data for each top cluster
    for cluster_id in cluster_counts["Cluster"]:
        cluster_df = df[df["Cluster"] == cluster_id]  # Filter data for the cluster
        file_path = os.path.join(feature_folder, f"Cluster_{cluster_id}.csv")
        cluster_df.to_csv(file_path, index=False)
        print(f"Saved: {file_path}")

    return cluster_counts  # Return top cluster summary if needed


# # Example Usage:
# df = pd.read_csv("data/Gemstat_Data_Cleaned_Raw/All_lakes_clustered_haversine.csv")

# # Run the function for different features
# process_and_save_top_clusters(df, "Chl-a")
# process_and_save_top_clusters(df, "TURB")
# process_and_save_top_clusters(df, "DOC", num_clusters=3)  # Example with 3 clusters
