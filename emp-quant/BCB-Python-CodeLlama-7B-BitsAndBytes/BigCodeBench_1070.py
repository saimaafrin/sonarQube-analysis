
import pandas as pd
from random import shuffle

# Constants
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def task_func(list_of_lists):
    # Create a list of DataFrames
    dataframes = []

    # Iterate over the sublists in 'list_of_lists'
    for sublist in list_of_lists:
        # Create a new DataFrame with columns named as per the elements of the sublist
        df = pd.DataFrame(columns=sublist)

        # Fill each column with shuffled values from 'POSSIBLE_VALUES'
        for col in df.columns:
            df[col] = shuffle(POSSIBLE_VALUES)

        # Add the DataFrame to the list of DataFrames
        dataframes.append(df)

    return dataframes

# Print the list of DataFrames
print(dataframes)