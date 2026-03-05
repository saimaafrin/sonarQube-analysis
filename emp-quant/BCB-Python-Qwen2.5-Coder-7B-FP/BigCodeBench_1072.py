import pandas as pd
import numpy as np
def task_func(list_of_lists):
    series_list = []
    for sublist in list_of_lists:
        # Create a Series with unique integers from 1 to the length of the sublist
        series = pd.Series(np.arange(1, len(sublist) + 1), index=sublist)
        # Shuffle the Series in-place
        series.sample(frac=1, random_state=42, inplace=True)
        series_list.append(series)
    return series_list
list_of_lists = [['a', 'b', 'c'], ['d', 'e'], ['f', 'g', 'h', 'i']]