
import pandas as pd
from random import shuffle

# Constants
POSSIBLE_VALUES = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]

def task_func(list_of_lists):
    # Create a list of DataFrames
    data_frames = []

    # Iterate over the sublists in list_of_lists
    for sublist in list_of_lists:
        # Create a new DataFrame with the same number of columns as sublist
        df = pd.DataFrame(index=range(len(sublist)), columns=sublist)

        # Fill each column with shuffled values from POSSIBLE_VALUES
        for col in df.columns:
            df[col] = shuffle(POSSIBLE_VALUES)

        # Add the DataFrame to the list of DataFrames
        data_frames.append(df)

    return data_frames