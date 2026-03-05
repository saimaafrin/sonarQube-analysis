from sklearn.preprocessing import MinMaxScaler
import pandas as pd
def task_func(l):
    """
    Scale the input field to the range [0, 1] and display it as a DataFrame.
    """
    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Scale the input list
    scaled_list = scaler.fit_transform(l)

    # Create a DataFrame from the scaled list
    df = pd.DataFrame(scaled_list, columns=['Scaled Values'])

    return df
l = [1, 2, 3, 4, 5]