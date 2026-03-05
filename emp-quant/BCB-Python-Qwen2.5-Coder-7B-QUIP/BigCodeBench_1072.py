
import pandas as pd
import numpy as np

def task_func(list_of_lists):
    series_list = []
    for sublist in list_of_lists:
        # Create a list of unique integers from 1 to the length of the sublist
        values = list(range(1, len(sublist) + 1))
        # Shuffle the list using numpy's random shuffle
        np.random.shuffle(values)
        # Create a pandas Series with the shuffled values
        series = pd.Series(values, index=sublist)
        series_list.append(series)
    return series_list

# Print the resulting list of Series
for series in series_list:
    print(series)