
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def task_func(d):
    if not d:
        return pd.DataFrame()
    
    # Extract the values for scaling
    values = [[item['x'], item['y'], item['z']] for item in d]
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the values
    scaled_values = scaler.fit_transform(values)
    
    # Create a DataFrame with the scaled values
    df_scaled = pd.DataFrame(scaled_values, columns=['x', 'y', 'z'])
    
    return df_scaled