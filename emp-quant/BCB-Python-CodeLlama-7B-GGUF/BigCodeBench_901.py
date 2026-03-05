
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Updated function to handle empty input list
def task_func(d):
    if not d:
        return pd.DataFrame()

    scaler = MinMaxScaler()
    scaled_data = scaler.fit_transform(pd.DataFrame(d))
    return pd.DataFrame(scaled_data, columns=['x', 'y', 'z'])