import pandas as pd
from random import shuffle
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
def task_func(list_of_lists):
    """
    Generates a list of pandas DataFrames, each created from a sublist in 'list_of_lists'.
    Each DataFrame has columns named as per the elements of the sublist, and each column is filled with
    randomly shuffled values from 'POSSIBLE_VALUES'.
    
    Parameters:
    list_of_lists (list of list of str): A list of lists, where each sublist contains column names.
    
    Returns:
    list of pandas.DataFrame: A list where each element is a DataFrame with columns as specified
    in 'list_of_lists', and each column contains shuffled values from 'POSSIBLE_VALUES'.
    """
    dataframes = []
    for sublist in list_of_lists:
        # Shuffle the values for each column
        shuffled_values = POSSIBLE_VALUES.copy()
        shuffle(shuffled_values)
        # Create a dictionary to hold the column data
        column_data = {col: shuffled_values for col in sublist}
        # Create a DataFrame from the dictionary
        df = pd.DataFrame(column_data)
        dataframes.append(df)
    return dataframes
list_of_lists = [["A", "B"], ["C", "D", "E"], ["F", "G", "H", "I"]]