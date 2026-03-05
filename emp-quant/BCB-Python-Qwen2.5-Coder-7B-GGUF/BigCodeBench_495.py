
import pandas as pd
import numpy as np

def task_func(days, random_seed=0):
    np.random.seed(random_seed)
    dates = pd.date_range(start='2023-01-01', periods=days)
    data = {
        'Groceries': np.random.randint(0, 101, size=days),
        'Entertainment': np.random.randint(0, 101, size=days),
        'Rent': np.random.randint(0, 101, size=days),
        'Utilities': np.random.randint(0, 101, size=days),
        'Miscellaneous': np.random.randint(0, 101, size=days)
    }
    df = pd.DataFrame(data, index=dates)
    return df