import pandas as pd
from random import shuffle
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
def task_func(list_of_lists):
    """
    Generates a list of pandas DataFrames, each created from a sublist in 'list_of_lists'.
    Each DataFrame has columns named as per the elements of the sublist, and each column is filled with
    randomly shuffled values from 'POSSIBLE_VALUES'.
    
    :param list_of_lists: List of lists, where each sublist contains column names for a DataFrame.
    :return: List of pandas.DataFrame
    """
    # Shuffle the possible values once to ensure all columns have the same order
    shuffled_values = POSSIBLE_VALUES[:]
    shuffle(shuffled_values)
    
    # Create a list to hold the DataFrames
    dataframes = []
    
    # Create a DataFrame for each sublist in list_of_lists
    for sublist in list_of_lists:
        # Create a dictionary to hold the column data
        column_data = {col: shuffled_values for col in sublist}
        # Create a DataFrame from the dictionary
        df = pd.DataFrame(column_data)
        # Append the DataFrame to the list
        dataframes.append(df)
    
    return dataframes
list_of_lists = [["A", "B"], ["C", "D", "E"], ["F", "G", "H", "I", "J"]]