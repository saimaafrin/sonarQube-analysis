
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data_dict, data_keys):
    """
    Normalize data specified by keys in a dictionary using MinMax scaling and plot the results.
    
    Parameters:
    - data_dict (dict): Dictionary containing the data to be normalized.
    - data_keys (list): List of keys whose corresponding values need to be normalized.
    
    Returns:
    - tuple: A tuple containing a DataFrame of normalized values and a matplotlib Axes object representing a plot of the normalized data.
    
    Raises:
    - ValueError: If no keys in `data_keys` are found in `data_dict`.
    """
    # Check if any of the keys exist in the dictionary
    if not any(key in data_dict for key in data_keys):
        raise ValueError("No keys in `data_keys` are found in `data_dict`.")
    
    # Extract the data to be normalized
    data_to_normalize = {key: data_dict[key] for key in data_keys}
    
    # Create a DataFrame from the extracted data
    df = pd.DataFrame(data_to_normalize)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    normalized_data = scaler.fit_transform(df)
    
    # Create a new DataFrame with the normalized data
    normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
    
    # Plot the original and normalized data
    fig, ax = plt.subplots(2, 1, figsize=(10, 8))
    
    # Plot the original data
    df.plot(ax=ax[0], title='Original Data')
    
    # Plot the normalized data
    normalized_df.plot(ax=ax[1], title='Normalized Data')
    
    # Adjust layout
    plt.tight_layout()
    
    return normalized_df, ax[1]

    try:
        normalized_df, ax = task_func(data_dict, data_keys)
        print(normalized_df)
        plt.show()
    except ValueError as e:
        print(e)