from sklearn.preprocessing import MinMaxScaler
import pandas as pd
def task_func(l):
    """
    Scale the input list to the range [0, 1] and return it as a DataFrame with a single column named 'Scaled Values'.
    
    Parameters:
    l (list): A list of numerical values to be scaled.
    
    Returns:
    DataFrame: A pandas DataFrame containing the scaled values.
    """
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Reshape the list to a 2D array as MinMaxScaler expects a 2D array
    l_reshaped = np.array(l).reshape(-1, 1)
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(l_reshaped)
    
    # Convert the scaled data to a DataFrame
    df_scaled = pd.DataFrame(scaled_data, columns=['Scaled Values'])
    
    return df_scaled
l = [10, 20, 30, 40, 50]