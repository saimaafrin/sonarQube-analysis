
import pandas as pd
import numpy as np
import itertools

def task_func(T1, row_num=50, seed=None):
    # Convert elements in 'T1' to integers
    T1 = [int(i) for i in T1]

    # Create a Pandas DataFrame with random numbers
    df = pd.DataFrame(np.random.randint(0, 100, size=(row_num, len(T1))), columns=T1)

    return df