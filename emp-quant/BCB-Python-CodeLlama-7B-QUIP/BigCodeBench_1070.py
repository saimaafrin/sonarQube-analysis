
import pandas as pd
from random import shuffle
# Constants
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
def task_func(list_of_lists):
    # Create a list of DataFrames
    list_of_dataframes = []
    for sublist in list_of_lists:
        # Create a DataFrame with the same number of columns as the sublist
        dataframe = pd.DataFrame(index=range(len(sublist)))
        for i, element in enumerate(sublist):
            # Create a column with the same name as the element in the sublist
            dataframe[element] = shuffle(POSSIBLE_VALUES)
        list_of_dataframes.append(dataframe)
    return list_of_dataframes