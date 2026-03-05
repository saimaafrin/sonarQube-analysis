import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(data):
    # Create a StandardScaler object
    scaler = StandardScaler()

    # Scale the numeric columns of the dataframe
    scaled_data = scaler.fit_transform(data)

    # Create a new dataframe with the scaled numeric columns
    scaled_data = pd.DataFrame(scaled_data, columns=data.columns)

    return scaled_data
data = pd.DataFrame({'A': [1, 2, 3, 4, 5],
                     'B': [1.5, 2.5, 3.5, 4.5, 5.5],
                     'C': ['a', 'b', 'c', 'd', 'e'],
                     'D': [1, 2, 3, 4, 5]})