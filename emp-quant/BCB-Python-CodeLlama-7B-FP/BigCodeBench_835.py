import numpy as np
import pandas as pd
import pytest
def task_func(n_rows, remove_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    """
    Generate a DataFrame with columns 'columns' and fill them with random integer values between 0 and 100.
    Remove some columns based on the provided indexes.
    """
    if random_seed is not None:
        np.random.seed(random_seed)
    df = pd.DataFrame(np.random.randint(0, 100, size=(n_rows, len(columns))), columns=columns)
    df = df.drop(columns=remove_cols)
    return df