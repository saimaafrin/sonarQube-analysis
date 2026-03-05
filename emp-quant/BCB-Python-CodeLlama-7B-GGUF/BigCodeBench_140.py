
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(df, cols):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("'df' must be a DataFrame")
    if not isinstance(cols, list):
        raise ValueError("'cols' must be a list")
    if not all(col in df.columns for col in cols):
        raise ValueError("Columns in 'cols' must exist in 'df'")

    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(df[cols])
    scaled_df = pd.DataFrame(scaled_df, columns=cols)
    return scaled_df