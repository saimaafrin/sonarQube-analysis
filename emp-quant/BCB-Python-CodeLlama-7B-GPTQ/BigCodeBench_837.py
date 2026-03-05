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

    # Generate random values for the DataFrame
    data = np.random.rand(n_rows, len(columns))

    # Create a DataFrame from the random values
    df = pd.DataFrame(data, columns=columns)

    # Scale the selected columns
    scaler = StandardScaler()
    if scale_cols:
        for col in scale_cols:
            df[col] = scaler.fit_transform(df[col].values.reshape(-1, 1))

    return df