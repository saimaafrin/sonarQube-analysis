from sklearn.preprocessing import MinMaxScaler
import pandas as pd
def task_func(l):
    """
    Scales the input list to the range [0, 1] and returns it as a pandas DataFrame with a single column named 'Scaled Values'.
    
    Parameters:
    l (list): A list of numerical values to be scaled.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the scaled values.
    """
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Reshape the list to a 2D array as MinMaxScaler expects a 2D array
    l_reshaped = np.array(l).reshape(-1, 1)
    
    # Fit and transform the data
    scaled_values = scaler.fit_transform(l_reshaped)
    
    # Create a DataFrame with the scaled values
    df = pd.DataFrame(scaled_values, columns=['Scaled Values'])
    
    return df