
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(list_of_pairs):
    if not list_of_pairs:
        raise Exception("Input array is empty")
    
    categories = [pair[0] for pair in list_of_pairs]
    values = [pair[1] for pair in list_of_pairs]
    
    try:
        values = pd.to_numeric(values)
    except ValueError:
        raise ValueError("Values are not numeric")
    
    scaler = MinMaxScaler()
    normalized_values = scaler.fit_transform(values.values.reshape(-1, 1))
    
    result_df = pd.DataFrame({
        'Category': categories,
        'Value': normalized_values.flatten()
    })
    
    return result_df