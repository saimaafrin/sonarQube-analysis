
import pandas as pd
from random import shuffle

# Constants
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def task_func(list_of_lists):
    # Create a list to hold the DataFrames
    dataframes = []
    
    # Iterate over each sublist in list_of_lists
    for sublist in list_of_lists:
        # Shuffle the values in POSSIBLE_VALUES
        shuffled_values = POSSIBLE_VALUES.copy()
        shuffle(shuffled_values)
        
        # Create a DataFrame with columns named as per the elements of the sublist
        df = pd.DataFrame({col: shuffled_values for col in sublist})
        
        # Append the DataFrame to the list
        dataframes.append(df)
    
    # Return the list of DataFrames
    return dataframes