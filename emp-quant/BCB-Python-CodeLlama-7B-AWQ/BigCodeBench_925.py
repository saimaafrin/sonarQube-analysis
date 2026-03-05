import pandas as pd
import numpy as np
def task_func(data_size=1000, column_names=['A', 'B', 'C', 'D', 'E'], seed=0):
    np.random.seed(seed)
    data = np.random.randint(1, 100, size=(data_size, len(column_names)))
    data[data < 10] = -1
    return pd.DataFrame(data, columns=column_names)