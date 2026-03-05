
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(data):
    scaler = StandardScaler()
    numeric_cols = data.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        try:
            data[col] = pd.to_numeric(data[col], errors='coerce')
            data[col] = scaler.fit_transform(data[col].values.reshape(-1, 1))
        except ValueError:
            continue
    return data