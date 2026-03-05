
import pandas as pd
import time
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')

def task_func(data, letter):
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Filter rows where the 'Name' column starts with the specified letter
    filtered_df = df[df['Name'].str.startswith(letter)]
    
    # Return the filtered 'Name' column as a Series
    return filtered_df['Name']