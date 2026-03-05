
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(d):
    # Check if the input list is empty
    if not d:
        return pd.DataFrame()

    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()

    # Extract the values for 'x', 'y', and 'z'
    x_values = [item['x'] for item in d]
    y_values = [item['y'] for item in d]
    z_values = [item['z'] for item in d]

    # Reshape the data for scaling
    data = np.array([x_values, y_values, z_values]).T

    # Fit and transform the data
    scaled_data = scaler.fit_transform(data)

    # Create a new DataFrame with the scaled values
    result_df = pd.DataFrame(scaled_data, columns=['x', 'y', 'z'])

    return result_df