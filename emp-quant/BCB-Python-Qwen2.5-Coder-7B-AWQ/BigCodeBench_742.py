import pandas as pd
from sklearn.preprocessing import MinMaxScaler
def task_func(list_of_pairs):
    # Check if the input array is empty
    if not list_of_pairs:
        raise Exception("Input array is empty")
    
    # Check if all values are numeric
    for pair in list_of_pairs:
        if not all(isinstance(x, (int, float)) for x in pair):
            raise ValueError("Values are not numeric")
    
    # Create a DataFrame from the list of pairs
    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the 'Value' column
    df['Value'] = scaler.fit_transform(df[['Value']])
    
    return df