
import pandas as pd
import time
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
def task_func(data, letter):
    # Convert dict to DataFrame
    df = pd.DataFrame(data)
    # Filter rows where 'Name' column starts with specified letter
    filtered_df = df[df['Name'].str.startswith(letter)]
    # Extract 'Name' column from filtered DataFrame
    filtered_series = filtered_df['Name']
    return filtered_series