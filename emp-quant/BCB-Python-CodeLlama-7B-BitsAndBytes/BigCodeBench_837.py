
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(n_rows, scale_cols, columns=['A', 'B', 'C', 'D', 'E'], random_seed=None):
    # Generate random data for the DataFrame
    data = np.random.rand(n_rows, len(columns))

    # Create a DataFrame with the random data
    df = pd.DataFrame(data, columns=columns)

    # Scale the selected columns using StandardScaler
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(df[scale_cols])

    # Add the scaled columns back to the original DataFrame
    df[scale_cols] = scaled_df

    return df