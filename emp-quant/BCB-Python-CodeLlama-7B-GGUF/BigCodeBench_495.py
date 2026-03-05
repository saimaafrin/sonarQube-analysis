
import pandas as pd
import numpy as np

def task_func(days, random_seed=0):
    np.random.seed(random_seed)
    df = pd.DataFrame(index=pd.date_range(start='2023-01-01', periods=days))
    df['Groceries'] = np.random.randint(0, 101, size=days)
    df['Entertainment'] = np.random.randint(0, 101, size=days)
    df['Rent'] = np.random.randint(0, 101, size=days)
    df['Utilities'] = np.random.randint(0, 101, size=days)
    df['Miscellaneous'] = np.random.randint(0, 101, size=days)
    return df