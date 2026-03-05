
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(data):
    scaler = StandardScaler()
    numeric_columns = data.select_dtypes(include=[float, int]).columns
    for col in numeric_columns:
        try:
            data[col] = pd.to_numeric(data[col], errors='coerce')
            data[col] = scaler.fit_transform(data[col].values.reshape(-1, 1))
        except ValueError:
            pass
    return data