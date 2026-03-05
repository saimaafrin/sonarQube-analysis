import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    """
    Generate a DataFrame with columns 'columns' and fill them with random values.
    Scale the columns at the provided indexes with sklearn StandardScaler.
    If scale_cols is empty no column is scaled.
    """
    np.random.seed(random_seed)
    df = pd.DataFrame(np.random.randn(n_rows, len(columns)), columns=columns)
    scaler = StandardScaler()
    if scale_cols:
        for col in scale_cols:
            df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))
    return df