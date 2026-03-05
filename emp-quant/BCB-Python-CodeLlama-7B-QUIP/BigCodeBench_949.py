
import numpy as np
import pandas as pd

def task_func(rows, columns, seed=None):
    if seed:
        np.random.seed(seed)
    data = np.random.rand(rows, columns)
    return pd.DataFrame(data)