
import pandas as pd
from sklearn.preprocessing import LabelEncoder

def task_func(data):
    # Initialize the LabelEncoder
    encoder = LabelEncoder()
    
    # Fit and transform the data
    encoded_data = encoder.fit_transform(data)
    
    # Create a DataFrame with the original data and the encoded data
    result_df = pd.DataFrame({'Category': data, 'Encoded': encoded_data})
    
    return result_df