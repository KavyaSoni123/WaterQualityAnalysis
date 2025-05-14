import pandas as pd
import ee
from datetime import timedelta
import datetime


def extract_dates(df):
    return df["Date"].dt.date.unique()
