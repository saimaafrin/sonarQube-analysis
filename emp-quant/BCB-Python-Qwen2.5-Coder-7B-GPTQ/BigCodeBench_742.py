import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(list_of_pairs):
    # Check if the input list is empty
    if not list_of_pairs:
        raise Exception("Input array is empty")
    
    # Extract categories and values from the list of pairs
    categories = [pair[0] for pair in list_of_pairs]
    values = [pair[1] for pair in list_of_pairs]
    
    # Check if all values are numeric
    if not all(isinstance(value, (int, float)) for value in values):
        raise ValueError("Values are not numeric")
    
    # Create a DataFrame
    df = pd.DataFrame({'Category': categories, 'Value': values})
    
    # Initialize and fit the MinMaxScaler
    scaler = MinMaxScaler()
    df['Value'] = scaler.fit_transform(df[['Value']])
    
    return df