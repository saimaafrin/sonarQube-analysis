
from sklearn.preprocessing import MinMaxScaler
import pandas as pd

def task_func(l):
    # Create a DataFrame from the input list
    df = pd.DataFrame(l, columns=['Original Values'])
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the DataFrame
    scaled_df = scaler.fit_transform(df)
    
    # Create a new DataFrame with the scaled values and set the column name
    scaled_df = pd.DataFrame(scaled_df, columns=['Scaled Values'])
    
    # Return the scaled DataFrame
    return scaled_df