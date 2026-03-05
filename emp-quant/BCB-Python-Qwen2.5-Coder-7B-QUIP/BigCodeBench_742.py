
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.exceptions import NotFittedException

def task_func(list_of_pairs):
    if not list_of_pairs:
        raise ValueError("Input array is empty")
    
    # Check if all elements are numeric
    if not all(isinstance(item, (int, float)) for pair in list_of_pairs for item in pair):
        raise ValueError("Values are not numeric")
    
    # Create DataFrame
    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])
    
    # Initialize and fit the MinMaxScaler
    scaler = MinMaxScaler()
    scaler.fit(df[['Value']])
    
    # Transform the data and add to DataFrame
    df['Value'] = scaler.transform(df[['Value']])
    
    return df