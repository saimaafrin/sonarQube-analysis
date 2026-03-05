
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(data):
    # Create a list of numeric columns
    numeric_columns = [col for col in data.columns if data[col].dtype in (int, float)]

    # Create a StandardScaler object
    scaler = StandardScaler()

    # Scale the numeric columns
    scaled_data = scaler.fit_transform(data[numeric_columns])

    # Create a new dataframe with the scaled data
    scaled_data = pd.DataFrame(scaled_data, columns=numeric_columns)

    # Add the non-numeric columns to the scaled data
    scaled_data[data.columns.difference(numeric_columns)] = data[data.columns.difference(numeric_columns)]

    return scaled_data