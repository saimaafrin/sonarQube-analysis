
import pandas as pd
import numpy as np

def task_func(rows=100, columns=3):
    data = np.random.rand(rows, columns)
    df = pd.DataFrame(data, columns=['a', 'b', 'c'])
    return df