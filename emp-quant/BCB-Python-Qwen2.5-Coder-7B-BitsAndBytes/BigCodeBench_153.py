
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(data):
    """
    Transforms categorical data into a numerical format using LabelEncoder.

    Parameters:
    - data (list): A list of categorical data to be encoded.

    Returns:
    - DataFrame: A DataFrame with two columns 'Category' and 'Encoded'.
    """
    # Initialize the LabelEncoder
    encoder = LabelEncoder()
    
    # Fit and transform the data
    encoded_data = encoder.fit_transform(data)
    
    # Create a DataFrame with the original categories and their encoded values
    result_df = pd.DataFrame({
        'Category': data,
        'Encoded': encoded_data
    })
    
    return result_df