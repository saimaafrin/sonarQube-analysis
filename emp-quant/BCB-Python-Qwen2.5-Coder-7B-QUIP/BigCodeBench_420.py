
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(data):
    scaler = StandardScaler()
    for column in data.columns:
        try:
            data[column] = pd.to_numeric(data[column], errors='coerce')
            if data[column].dtype == 'float64':
                data[column] = scaler.fit_transform(data[column].values.reshape(-1, 1))
        except (TypeError, ValueError):
            pass
    return data