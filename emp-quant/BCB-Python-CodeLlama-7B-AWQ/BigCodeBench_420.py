import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(data):
    # Create a list of numeric columns
    numeric_columns = [col for col in data.columns if data[col].dtype in [np.float64, np.float32]]

    # Create a list of non-numeric columns
    non_numeric_columns = [col for col in data.columns if col not in numeric_columns]

    # Scale numeric columns
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(data[numeric_columns])

    # Create a new dataframe with scaled numeric columns
    scaled_data = pd.DataFrame(scaled_data, columns=numeric_columns)

    # Add non-numeric columns to the scaled dataframe
    for col in non_numeric_columns:
        scaled_data[col] = data[col]

    return scaled_data
data = pd.DataFrame({'A': [1, 2, 3], 'B': ['a', 'b', 'c'], 'C': [1.0, 2.0, 3.0]})