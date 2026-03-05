import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(data):
    scaler = StandardScaler()
    for column in data.columns:
        try:
            # Attempt to convert the column to float
            data[column] = data[column].astype(float)
            # Scale the column using StandardScaler
            data[column] = scaler.fit_transform(data[column].values.reshape(-1, 1))
        except ValueError:
            # If conversion to float fails, leave the column unchanged
            continue
    return data