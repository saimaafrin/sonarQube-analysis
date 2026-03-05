import pandas as pd
import time
def task_func(data, letter):
    """
    Filters rows in a dictionary where the 'Name' column values start with a specified letter.
    
    Parameters:
    - data (dict): A dictionary where each key is a unique identifier and the value is another dictionary containing 'Name' and other data.
    - letter (str): The letter to filter the 'Name' column values by.
    
    Returns:
    - pd.Series: A Series of filtered 'Name' column.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(list(data.values()))
    
    # Filter rows where the 'Name' column starts with the specified letter
    filtered_df = df[df['Name'].str.startswith(letter)]
    
    # Return the filtered 'Name' column as a Series
    return filtered_df['Name']
data = {
    1: {'Name': 'Alice', 'Age': 25},
    2: {'Name': 'Bob', 'Age': 30},
    3: {'Name': 'Charlie', 'Age': 35},
    4: {'Name': 'David', 'Age': 40},
    5: {'Name': 'Eve', 'Age': 45},
    6: {'Name': 'Frank', 'Age': 50},
    7: {'Name': 'Grace', 'Age': 55},
    8: {'Name': 'Hank', 'Age': 60},
    9: {'Name': 'Ivy', 'Age': 65},
    10: {'Name': 'Jack', 'Age': 70},
}
letter = 'A'