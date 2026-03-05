
from random import shuffle, randint
import pandas as pd

def task_func(l, n_groups = 5):
    shuffled_list = shuffle(l)
    series = pd.Series(l)
    for i in range(n_groups):
        series = series.iloc[n_groups:, :n_groups]
    return series