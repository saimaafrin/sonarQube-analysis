import pandas as pd
from random import shuffle
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
def task_func(list_of_lists):
    """
    Generates a list of pandas DataFrames from sublists in 'list_of_lists'.
    Each DataFrame has columns named as per the elements of the sublist,
    and each column is filled with randomly shuffled values from 'POSSIBLE_VALUES'.
    
    Parameters:
    - list_of_lists: A list of lists, where each sublist contains column names.
    
    Returns:
    - list of pandas.DataFrame: A list of DataFrames created as described.
    """
    # Shuffle the possible values to ensure randomness
    shuffled_values = POSSIBLE_VALUES[:]
    shuffle(shuffled_values)
    
    # Create a list to hold the DataFrames
    dataframes = []
    
    # Iterate over each sublist in list_of_lists
    for sublist in list_of_lists:
        # Create a dictionary to hold the column data
        column_data = {}
        
        # Iterate over each column name in the sublist
        for column_name in sublist:
            # Assign the shuffled values to the column
            column_data[column_name] = shuffled_values[:]
        
        # Create a DataFrame from the column data
        df = pd.DataFrame(column_data)
        
        # Append the DataFrame to the list
        dataframes.append(df)
    
    return dataframes
list_of_lists = [["A", "B"], ["C", "D", "E"], ["F", "G", "H", "I"]]