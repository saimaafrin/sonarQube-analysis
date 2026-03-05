import pandas as pd
import time
def task_func(data, letter):
    """
    Filters rows in a dictionary where the 'Name' column values start with a specified letter.
    First, convert the dict to a DataFrame and then filter rows in this DataFrame.
    """
    # Convert the dict to a DataFrame
    df = pd.DataFrame(data)
    # Filter rows in the DataFrame
    filtered_df = df[df['Name'].str.startswith(letter)]
    # Extract the 'Name' column from the filtered DataFrame
    filtered_series = filtered_df['Name']
    return filtered_series
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45]
}