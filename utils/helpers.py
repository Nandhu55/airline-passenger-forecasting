import pandas as pd


def get_dataset_information(df):

    return {

        "rows": df.shape[0],

        "columns": df.shape[1],

        "missing": df.isnull().sum().sum()

    }