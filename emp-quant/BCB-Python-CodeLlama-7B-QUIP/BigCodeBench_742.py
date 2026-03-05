
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_pairs):
    # Check if the input list is empty
    if len(list_of_pairs) == 0:
        raise Exception("Input list is empty")

    # Create a DataFrame from the list of pairs
    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])

    # Normalize the data using MinMaxScaler
    scaler = MinMaxScaler()
    df['Value'] = scaler.fit_transform(df['Value'].values.reshape(-1, 1))

    # Return the normalized DataFrame
    return df