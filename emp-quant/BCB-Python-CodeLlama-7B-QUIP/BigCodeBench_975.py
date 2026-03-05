
import numpy as np
import pandas as pd

def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    np.random.seed(seed)
    data = np.random.rand(rows, len(columns))
    data = data.reshape(rows, len(columns))
    data = data.sort(axis=1)
    return pd.DataFrame(data, columns=columns)