import os


def save_dataframe(df, save_path, file_name, file_format="csv"):
    """
    Saves a DataFrame to a specified location with a given name and format.

    Parameters:
        df (pd.DataFrame): The DataFrame to save.
        save_path (str): The directory where the file should be saved.
        file_name (str): The name of the file (without extension).
        file_format (str): The file format ('csv' or 'parquet'). Default is 'csv'.

    Returns:
        str: The full path of the saved file.
    """
    # Ensure the directory exists
    os.makedirs(save_path, exist_ok=True)

    # Construct the full file path
    full_path = os.path.join(save_path, f"{file_name}.{file_format}")

    # Save based on the specified format
    if file_format == "csv":
        df.to_csv(full_path, index=False)
    elif file_format == "parquet":
        df.to_parquet(full_path, index=False)
    else:
        raise ValueError("Unsupported file format! Use 'csv' or 'parquet'.")

    return full_path
