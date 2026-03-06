
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(l):
    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Scale the input list
    scaled_list = scaler.fit_transform(l)

    # Create a DataFrame from the scaled list
    df = pd.DataFrame({'Scaled Values': scaled_list})

    return df