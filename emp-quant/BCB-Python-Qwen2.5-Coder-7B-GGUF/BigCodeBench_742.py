
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_pairs):
    if not list_of_pairs:
        raise Exception("Input array is empty")
    
    categories = [pair[0] for pair in list_of_pairs]
    values = [pair[1] for pair in list_of_pairs]
    
    if not all(isinstance(val, (int, float)) for val in values):
        raise ValueError("Values are not numeric")
    
    df = pd.DataFrame({'Category': categories, 'Value': values})
    
    scaler = MinMaxScaler()
    df['Value'] = scaler.fit_transform(df[['Value']])
    
    return df