import pandas as pd
import numpy as np
def task_func(list_of_lists):
    series_list = []
    for sub_list in list_of_lists:
        series = pd.Series(np.random.permutation(len(sub_list)))
        series.index = sub_list
        series_list.append(series)
    return series_list
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]