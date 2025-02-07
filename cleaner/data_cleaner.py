import pandas as pd

def load_and_clean_data(lakeCSVPath, lakeMetaDataPath):
    data = pd.read_csv(lakeCSVPath, delimiter=';', header=None)
    data2 = data[[0, 1, 2, 4, 7, 8, 9]].copy()
    data2.columns = ["Station", "Date", "Time", "Parameter", "Value", "Unit", "Remarks"]
    data_pivoted = data2.pivot_table(
        index=["Station", "Date", "Time"],
        columns="Parameter",
        values="Value",
        aggfunc="first"
    ).reset_index()

    null_percentage = data_pivoted.isnull().sum() / len(data_pivoted) * 100
    columns_to_drop = null_percentage[null_percentage > 50].index
    data_pivoted = data_pivoted.drop(columns=columns_to_drop)

    threshold = 0.8 * data_pivoted.shape[1]
    data_pivoted = data_pivoted.dropna(thresh=threshold)

    data_pivoted['Date'] = pd.to_datetime(data_pivoted['Date'])
    data_pivoted['Time'] = pd.to_datetime(data_pivoted['Time'], format='%H:%M:%S', errors='coerce').dt.time

    excel = pd.read_excel(lakeMetaDataPath)
    excel = excel[['GEMS Station Number', 'Station Identifier', 'Latitude', 'Longitude']]

    data_pivoted = pd.merge(data_pivoted, excel, left_on='Station', right_on='GEMS Station Number', how='left')
    data_pivoted = data_pivoted.drop('GEMS Station Number', axis=1)
    
    return data_pivoted

def select_columns(cols,dataframe):
    return dataframe[cols]

def select_parameter_type(typecol, dataframe, allParametersPath):
    params = pd.read_csv(allParametersPath)
    col = list(params[params['Parameter Group'] == typecol]['Parameter Code'].unique())
    return dataframe[col]
