
import pandas as pd
from random import shuffle

# Constants
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def task_func(list_of_lists):
    # Shuffle the possible values only once
    shuffled_values = POSSIBLE_VALUES[:]
    shuffle(shuffled_values)
    
    # Create a list to hold the DataFrames
    dataframes = []
    
    for sublist in list_of_lists:
        # Create a dictionary to hold the column data
        column_data = {}
        
        # Assign shuffled values to each column based on the sublist
        for i, col_name in enumerate(sublist):
            column_data[col_name] = [shuffled_values[i]] * len(sublist)
        
        # Create a DataFrame from the column data
        df = pd.DataFrame(column_data)
        dataframes.append(df)
    
    return dataframes

# Print the result
for df in result:
    print(df)