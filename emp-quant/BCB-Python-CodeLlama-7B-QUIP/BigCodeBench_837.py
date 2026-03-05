
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    # Generate random values for the columns
    columns = [np.random.normal(0, 1, size=n_rows) for i in range(len(columns))]

    # Create a DataFrame with the columns and random values
    df = pd.DataFrame(columns, columns=columns)

    # Scale the selected columns with the StandardScaler
    if scale_cols:
        scaler = StandardScaler()
        for col in scale_cols:
            scaler.fit(df.iloc[:, col])
            df.iloc[:, col] = scaler.transform(df.iloc[:, col])

    return df