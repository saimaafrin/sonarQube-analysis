
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(data):
    # Create a StandardScaler object
    scaler = StandardScaler()

    # Initialize an empty dataframe to store the scaled data
    scaled_data = pd.DataFrame(columns=data.columns)

    # Loop through each column in the data
    for column in data.columns:
        # Check if the column is numeric
        if data[column].dtype == "float64":
            # Scale the column using the StandardScaler
            scaled_data[column] = scaler.fit_transform(data[column])
        else:
            # If the column is not numeric, leave it unchanged
            scaled_data[column] = data[column]

    return scaled_data