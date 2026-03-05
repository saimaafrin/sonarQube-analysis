import pandas as pd
from sklearn.preprocessing import LabelEncoder
def task_func(data):
    """
    Transforms categorical data into a numerical format using LabelEncoder.
    
    Parameters:
    - data: A list or array-like of categorical data.
    
    Returns:
    - A DataFrame with two columns: 'Category' and 'Encoded', where 'Category' contains the original data
      and 'Encoded' contains the numerical representation of the categories.
    """
    # Initialize the LabelEncoder
    encoder = LabelEncoder()
    
    # Fit and transform the data
    encoded_data = encoder.fit_transform(data)
    
    # Create a DataFrame with the original data and the encoded data
    result_df = pd.DataFrame({
        'Category': data,
        'Encoded': encoded_data
    })
    
    return result_df
data = ['apple', 'banana', 'apple', 'orange', 'banana', 'apple']