import pandas as pd
from random import shuffle
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
def task_func(list_of_lists):
    """
    Generate a list of pandas DataFrames, each created from a sublist in 'list_of_lists'.
    Each DataFrame has columns named as per the elements of the sublist, and each column is filled with randomly shuffled values from 'POSSIBLE_VALUES'.
    Note that:
        - The length of each DataFrame's columns is equal to the length of 'POSSIBLE_VALUES'.
        - Each column in the DataFrame has the same shuffled order of 'POSSIBLE_VALUES'.
    The function should output with:
        list of pandas.DataFrame: A list where each element is a DataFrame with columns as specified
        in 'list_of_lists', and each column contains shuffled values from 'POSSIBLE_VALUES'.
    """
    # Initialize an empty list to store the DataFrames
    dataframes = []

    # Iterate over the sublists in 'list_of_lists'
    for sublist in list_of_lists:
        # Initialize an empty list to store the column values
        column_values = []

        # Iterate over the elements in the sublist
        for element in sublist:
            # Append a shuffled copy of 'POSSIBLE_VALUES' to the column values
            column_values.append(shuffle(POSSIBLE_VALUES))

        # Create a DataFrame with the column values
        dataframe = pd.DataFrame(column_values, columns=sublist)

        # Append the DataFrame to the list of DataFrames
        dataframes.append(dataframe)

    # Return the list of DataFrames
    return dataframes
list_of_lists = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I", "J"]]