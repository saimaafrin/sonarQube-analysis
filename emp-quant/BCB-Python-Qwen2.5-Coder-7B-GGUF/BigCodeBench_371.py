
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(l):
    scaler = MinMaxScaler()
    scaled_values = scaler.fit_transform([l])
    scaled_df = pd.DataFrame(scaled_values, columns=['Scaled Values'])
    return scaled_df