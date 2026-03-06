
import pandas as pd
import numpy as np

def task_func(list_of_lists):
    series_list = []
    for sublist in list_of_lists:
        # Create an array of unique integers from 1 to the length of the sublist
        values = np.arange(1, len(sublist) + 1)
        # Shuffle the array in-place
        np.random.shuffle(values)
        # Create a pandas Series with the shuffled values and the sublist as index
        series = pd.Series(values, index=sublist)
        series_list.append(series)
    return series_list