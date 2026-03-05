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

    # Scale the 'Age' and 'Income' columns for each group by 'id'
    scaled_df = df.groupby('id')['Age', 'Income'].transform(scaler.fit_transform)

    # Create a histogram of the scaled 'Income' column
    hist_data = scaled_df['Income'].hist(bins=20, density=True)

    # Return the scaled DataFrame and the histogram data
    return scaled_df, hist_data
df = pd.DataFrame({'id': [1, 1, 2, 2, 3, 3],
                   'Age': [25, 32, 30, 35, 20, 25],
                   'Income': [50000, 60000, 40000, 30000, 20000, 35000]})