
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(data):
    # Create a copy of the input dataframe
    scaled_data = data.copy()

    # Get a list of numeric columns
    numeric_columns = [col for col in data.columns if data[col].dtype.kind in 'biufc']

    # Scale the numeric columns using StandardScaler
    for col in numeric_columns:
        try:
            scaler = StandardScaler()
            scaled_data[col] = scaler.fit_transform(data[col].astype(float))
        except ValueError:
            # If any value in the column cannot be converted to float, leave the column unchanged
            pass

    return scaled_data