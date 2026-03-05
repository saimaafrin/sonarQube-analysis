
import pandas as pd
import time
# Constants
LETTERS = list('abcdefghijklmnopqrstuvwxyz')
def task_func(data, letter):
    # Convert the dict to a DataFrame
    df = pd.DataFrame(data)
    # Filter the rows where the 'Name' column values start with the specified letter
    df_filtered = df[df['Name'].str.startswith(letter)]
    # Return the filtered 'Name' column
    return df_filtered['Name']