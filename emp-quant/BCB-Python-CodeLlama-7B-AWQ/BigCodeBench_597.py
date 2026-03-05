import pandas as pd
import time
def task_func(data, letter):
    """
    Filters rows in a dictionary where the 'Name' column values start with a specified letter.
    First, convert the dict to a DataFrame and then filter rows in this DataFrame.
    """
    # Convert the dict to a DataFrame
    df = pd.DataFrame(data)
    # Filter rows in the DataFrame where the 'Name' column values start with the specified letter
    df = df[df['Name'].str.startswith(letter)]
    # Return the filtered 'Name' column as a Series
    return df['Name']
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank'],
        'Age': [24, 30, 35, 42, 29, 45]}
letter = 'B'