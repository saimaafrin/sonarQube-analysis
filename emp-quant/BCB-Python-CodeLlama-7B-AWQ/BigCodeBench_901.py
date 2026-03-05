import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(d):
    # Create a DataFrame from the input list of dictionaries
    df = pd.DataFrame(d)
    # Create a MinMaxScaler object
    scaler = MinMaxScaler()
    # Scale the values in the DataFrame using the MinMaxScaler
    scaled_df = scaler.fit_transform(df)
    # Return the scaled DataFrame
    return scaled_df