import pandas as pd
import ee
from datetime import timedelta
import datetime


# Function to extract coordinates for a specific date
def extract_coor(date, df):
    # Filter the dataframe where the date matches
    filtered_data = df[df["Date"].dt.date == date][["Longitude", "Latitude"]]
    # Convert the filtered data to a list of tuples
    coordinates = list(filtered_data.itertuples(index=False, name=None))
    return coordinates
