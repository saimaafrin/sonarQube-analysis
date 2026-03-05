import pandas as pd
import matplotlib.pyplot as plt
def task_func(data, column_name="target_column"):
    """
    Converts a given JSON data into a Pandas DataFrame and plots a histogram of a specified column.
    Handles non-numeric columns by converting them to categorical type and then to numeric codes.
    Raises ValueError if the specified column name does not exist in the DataFrame.
    
    Parameters:
    - data: A string containing JSON data.
    - column_name: A string representing the name of the column to plot the histogram for.
    
    Returns:
    - DataFrame: A pandas DataFrame created from the input JSON data.
    - Axes: A matplotlib Axes object showing the histogram plot of the specified column.
    """
    # Convert JSON data to DataFrame
    df = pd.read_json(data)
    
    # Check if the specified column exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the DataFrame.")
    
    # Convert non-numeric columns to categorical and then to numeric codes
    for col in df.columns:
        if not pd.api.types.is_numeric_dtype(df[col]):
            df[col] = pd.Categorical(df[col]).codes
    
    # Plot histogram for the specified column
    ax = df[column_name].hist(bins=10, edgecolor='black')
    ax.set_title(f'Histogram of {column_name}')
    ax.set_xlabel(column_name)
    
    return df, ax