import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(data_dict, data_keys):
    """
    Normalize data specified by keys in a dictionary using MinMax scaling and plot the results.
    
    Parameters:
    - data_dict: A dictionary containing the data to be normalized.
    - data_keys: A list of keys in data_dict to be normalized.
    
    Returns:
    - A tuple containing a DataFrame of normalized values and a matplotlib Axes object representing a plot of the normalized data.
    
    Raises:
    - ValueError: If no keys in `data_keys` are found in `data_dict`.
    """
    # Check if all keys are in the dictionary
    if not all(key in data_dict for key in data_keys):
        raise ValueError("Not all keys in data_keys are found in data_dict.")
    
    # Extract the data to be normalized
    data_to_normalize = {key: data_dict[key] for key in data_keys}
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_to_normalize)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    normalized_data = scaler.fit_transform(df)
    
    # Convert the normalized data back to a DataFrame
    normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
    
    # Plot the normalized data
    fig, ax = plt.subplots()
    normalized_df.plot(ax=ax)
    
    return normalized_df, ax
data_dict = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [5, 4, 3, 2, 1],
    'feature3': [2, 3, 4, 5, 6]
}
data_keys = ['feature1', 'feature2']