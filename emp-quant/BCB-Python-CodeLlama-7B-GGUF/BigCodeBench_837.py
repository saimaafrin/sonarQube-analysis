
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    # Generate random data
    if random_seed is not None:
        np.random.seed(random_seed)
    data = np.random.rand(n_rows, len(columns))

    # Create DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Scale selected columns
    scaler = StandardScaler()
    for col in scale_cols:
        df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))

    return df