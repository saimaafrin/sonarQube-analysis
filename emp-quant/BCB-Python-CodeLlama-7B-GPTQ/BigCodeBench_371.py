from sklearn.preprocessing import MinMaxScaler
import pandas as pd
def task_func(l):
    """
    Scale the input field to the range [0, 1] and display it as a DataFrame.
    Note that: The return DataFrame use 'Scaled Values' as the column name.
    """
    scaler = MinMaxScaler()
    scaled_values = scaler.fit_transform(l)
    df = pd.DataFrame(scaled_values, columns=['Scaled Values'])
    return df
l = [1, 2, 3, 4, 5]