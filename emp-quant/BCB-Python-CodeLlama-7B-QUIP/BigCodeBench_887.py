
import pandas as pd
import numpy as np
import itertools

def task_func(T1, row_num=50, seed=None):
    if seed is None:
        seed = np.random.randint(1, 10000)
    df = pd.DataFrame(np.random.randint(1, 100, size=(row_num, len(T1))), columns=T1)
    return df

T1 = (('1', '12'), ('1', '-12'))
df = task_func(T1, row_num=6, seed=21)
print(df)