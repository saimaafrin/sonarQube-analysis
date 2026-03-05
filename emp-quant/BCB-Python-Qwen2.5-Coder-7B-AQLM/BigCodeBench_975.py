
import numpy as np
import pandas as pd

def task_func(rows, columns=["A", "B", "C", "D", "E"], seed=0) -> pd.DataFrame:
    np.random.seed(seed)
    data = np.random.rand(rows, len(columns))
    df = pd.DataFrame(data, columns=columns)
    df.columns = sorted(df.columns)
    return df