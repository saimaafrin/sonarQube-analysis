
import pandas as pd
import numpy as np

def task_func(list_of_lists):
    series_list = []
    for sublist in list_of_lists:
        # Create a Series with unique integers from 1 to the length of the sublist
        series = pd.Series(np.arange(1, len(sublist) + 1))
        # Shuffle the Series in-place
        np.random.shuffle(series.values)
        # Set the index of the Series to the elements of the sublist
        series.index = sublist
        series_list.append(series)
    return series_list