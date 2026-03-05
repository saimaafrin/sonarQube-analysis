
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(l):
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Reshape the list to a 2D array as MinMaxScaler expects a 2D array
    l_reshaped = np.array(l).reshape(-1, 1)
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(l_reshaped)
    
    # Convert the scaled data to a pandas DataFrame
    df = pd.DataFrame(scaled_data, columns=['Scaled Values'])
    
    return df