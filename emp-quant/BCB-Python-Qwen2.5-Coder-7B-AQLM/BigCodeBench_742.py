
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_pairs):
    if not list_of_pairs:
        raise Exception("Input array is empty")
    
    for pair in list_of_pairs:
        if not all(isinstance(item, (int, float)) for item in pair):
            raise ValueError("Values are not numeric")
    
    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])
    scaler = MinMaxScaler()
    df['Value'] = scaler.fit_transform(df[['Value']])
    
    return df