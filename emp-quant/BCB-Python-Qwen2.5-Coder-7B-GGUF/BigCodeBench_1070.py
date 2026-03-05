
import pandas as pd
from random import shuffle

# Constants
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def task_func(list_of_lists):
    # Shuffle the possible values to ensure the same order for each column
    shuffled_values = POSSIBLE_VALUES[:]
    shuffle(shuffled_values)
    
    # Create a list to hold the DataFrames
    dataframes = []
    
    # Iterate over each sublist in list_of_lists
    for sublist in list_of_lists:
        # Create a dictionary to hold the column data
        column_data = {}
        
        # Iterate over each element in the sublist
        for element in sublist:
            # Assign the shuffled values to each column
            column_data[element] = shuffled_values[:]
        
        # Create a DataFrame from the column data
        df = pd.DataFrame(column_data)
        
        # Append the DataFrame to the list
        dataframes.append(df)
    
    # Return the list of DataFrames
    return dataframes