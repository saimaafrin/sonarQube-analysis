import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
def task_func(df):
    """
    Scale the 'Age' and 'Income' columns between 0 and 1 for each group by 'id' in the provided pandas DataFrame.
    Additionally, create a histogram of the 'Income' column after scaling and return both the scaled DataFrame and the histogram data.
    """
    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Scale the 'Age' and 'Income' columns
    scaled_df = df.copy()
    scaled_df['Age'] = scaler.fit_transform(scaled_df['Age'].values.reshape(-1, 1))
    scaled_df['Income'] = scaler.fit_transform(scaled_df['Income'].values.reshape(-1, 1))

    # Create a histogram of the scaled 'Income' column
    histogram_data = np.histogram(scaled_df['Income'], bins=20)

    return scaled_df, histogram_data
df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3],
                   'Age': [25, 32, 33, 35, 26, 30],
                   'Income': [50000, 60000, 70000, 80000, 40000, 50000]})