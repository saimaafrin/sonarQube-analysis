import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    """
    Generate a DataFrame with columns 'columns' and fill them with random values.
    Scale the columns at the provided indexes with sklearn StandardScaler.
    If scale_cols is empty no column is scaled.
    """
    if random_seed is not None:
        np.random.seed(random_seed)

    df = pd.DataFrame(np.random.randn(n_rows, len(columns)), columns=columns)

    if scale_cols:
        scaler = StandardScaler()
        scaled_df = scaler.fit_transform(df.iloc[:, scale_cols])
        scaled_df = pd.DataFrame(scaled_df, columns=columns)
    else:
        scaled_df = df

    return scaled_df