
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data_dict, data_keys):
    """
    Normalize data specified by keys in a dictionary using MinMax scaling and plot the results.
    
    Parameters:
    data_dict (dict): A dictionary containing the data.
    data_keys (list): A list of keys to normalize.
    
    Returns:
    tuple: A tuple containing a DataFrame of normalized values and a matplotlib Axes object representing a plot of the normalized data.
    
    Raises:
    ValueError: If no keys in `data_keys` are found in `data_dict`.
    """
    # Check if any of the data_keys are in data_dict
    if not any(key in data_dict for key in data_keys):
        raise ValueError("No keys in data_keys are found in data_dict.")
    
    # Extract the data to be normalized
    data_to_normalize = {key: data_dict[key] for key in data_keys if key in data_dict}
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    normalized_data = scaler.fit_transform(list(data_to_normalize.values()))
    
    # Convert the normalized data to a DataFrame
    normalized_df = pd.DataFrame(normalized_data, columns=data_keys)
    
    # Plot the normalized data
    fig, ax = plt.subplots()
    normalized_df.plot(ax=ax)
    
    # Return the DataFrame and the plot
    return normalized_df, ax