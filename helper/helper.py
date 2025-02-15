def lookup_table(df, cluster):
    return df[df["Cluster"] == cluster][["Latitude", "Longitude", "Region", "Date"]]


def sort_cluster_by_feature(df, feature, top_n=5):
    filtered_df = df[df[f"{feature}"].notnull()]
    cluster_counts = filtered_df.groupby("Cluster").size()
    return cluster_counts.sort_values(ascending=False).head(top_n)


def compare_clusters(df, clusters_to_keep):
    filtered_df = df[df["Cluster"].isin(clusters_to_keep)]
    filtered_df = filtered_df.dropna(how="all")
    filtered_df = filtered_df.dropna(axis=1, how="all")
    missing_data_per_cluster = filtered_df.groupby("Cluster").apply(
        lambda x: x.isnull().mean() * 100
    )
    return missing_data_per_cluster.transpose()


def percentage_null_data_in_cluster(df, cluster):
    cluster_df = df[df["Cluster"] == 94]
    return cluster_df.isnull().mean() * 100
