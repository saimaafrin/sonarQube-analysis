
import pandas as pd
import numpy as np

def task_func(list_of_lists):
    series_list = []
    for sub_list in list_of_lists:
        series = pd.Series(sub_list)
        np.random.shuffle(series)
        series_list.append(series)
    return series_list