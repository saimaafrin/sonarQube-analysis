import pandas as pd
import os
import sys
def task_func(file_path: str, column_name: str) -> pd.DataFrame:
    """
    Load a CSV file into a Pandas DataFrame, replace all occurrences of the string '\n' with the string '<br>' in the specified column, and return the cleaned DataFrame.
    """
    # Load the CSV file into a Pandas DataFrame
    df = pd.read_csv(file_path)

    # Replace all occurrences of '\n' with '<br>' in the specified column
    df[column_name] = df[column_name].str.replace('\n', '<br>')

    # Return the cleaned DataFrame
    return df
file_path = 'data.csv'
column_name = 'text'