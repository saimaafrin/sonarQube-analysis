from sklearn.preprocessing import MinMaxScaler
import pandas as pd
def task_func(l):
    """
    Scale the input field to the range [0, 1] and display it as a DataFrame.
    """
    scaler = MinMaxScaler()
    scaled_l = scaler.fit_transform(l)
    df = pd.DataFrame(scaled_l, columns=['Scaled Values'])
    return df
l = [1, 2, 3, 4, 5]