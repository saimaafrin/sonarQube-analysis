import pandas as pd
from sklearn.preprocessing import LabelEncoder
def task_func(data):
    """
    Transforms categorical data into a numerical format using LabelEncoder.
    
    Parameters:
    - data: A list or array-like of categorical data.
    
    Returns:
    - A pandas DataFrame with two columns: 'Category' and 'Encoded'.
    """
    # Initialize the LabelEncoder
    label_encoder = LabelEncoder()
    
    # Fit and transform the data
    encoded_data = label_encoder.fit_transform(data)
    
    # Create a DataFrame with the original and encoded data
    result_df = pd.DataFrame({
        'Category': data,
        'Encoded': encoded_data
    })
    
    return result_df
data = ['apple', 'banana', 'cherry', 'apple', 'banana']