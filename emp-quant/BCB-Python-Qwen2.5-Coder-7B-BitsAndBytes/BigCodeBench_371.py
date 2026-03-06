
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(l):
    # Convert the list to a numpy array
    arr = np.array(l)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the array
    scaled_arr = scaler.fit_transform(arr.reshape(-1, 1))
    
    # Create a DataFrame with the scaled values
    df = pd.DataFrame(scaled_arr, columns=['Scaled Values'])
    
    return df