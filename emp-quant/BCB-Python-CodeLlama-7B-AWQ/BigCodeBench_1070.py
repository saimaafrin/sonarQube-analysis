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
    list_of_dataframes = []
    for sublist in list_of_lists:
        dataframe = pd.DataFrame(columns=sublist)
        for column in dataframe.columns:
            dataframe[column] = shuffle(POSSIBLE_VALUES)
        list_of_dataframes.append(dataframe)
    return list_of_dataframes
list_of_lists = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I", "J"]]