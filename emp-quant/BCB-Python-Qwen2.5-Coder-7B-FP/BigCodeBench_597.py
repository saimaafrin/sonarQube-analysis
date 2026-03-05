import pandas as pd
import time
def task_func(data, letter):
    """
    Filters rows in a dictionary where the 'Name' column values start with a specified letter.
    
    Parameters:
    - data (dict): A dictionary with a 'Name' column.
    - letter (str): The specified letter to filter the 'Name' column values by.
    
    Returns:
    - pd.Series: A Series of filtered 'Name' column.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Filter rows where the 'Name' column values start with the specified letter
    filtered_df = df[df['Name'].str.startswith(letter)]
    
    # Return the filtered 'Name' column as a Series
    return filtered_df['Name']
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eve'],
    'Age': [25, 30, 35, 40, 45]
}
letter = 'A'