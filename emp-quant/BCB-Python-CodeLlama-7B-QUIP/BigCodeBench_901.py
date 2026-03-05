
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Updated function to handle empty input list
def task_func(d):
    # Initialize MinMaxScaler
    scaler = MinMaxScaler()
    # Scale the data
    scaled_data = scaler.fit_transform(d)
    # Create a DataFrame
    df = pd.DataFrame(scaled_data)
    return df