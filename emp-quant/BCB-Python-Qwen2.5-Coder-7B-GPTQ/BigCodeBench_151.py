import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt
def task_func(data_dict, data_keys):
    """
    Normalize data specified by keys in a dictionary using MinMax scaling and plot the results.
    
    Parameters:
    - data_dict (dict): A dictionary containing the data to be normalized.
    - data_keys (list): A list of keys in the dictionary whose values are to be normalized.
    
    Returns:
    - tuple: A tuple containing a DataFrame of normalized values and a matplotlib Axes object representing a plot of the normalized data.
    
    Raises:
    - ValueError: If no keys in `data_keys` are found in `data_dict`.
    """
    # Check if any of the keys are in the dictionary
    if not any(key in data_dict for key in data_keys):
        raise ValueError("No keys in data_keys are found in data_dict.")
    
    # Extract the data to be normalized
    data_to_normalize = {key: data_dict[key] for key in data_keys if key in data_dict}
    
    # Create a DataFrame from the data to be normalized
    df = pd.DataFrame(data_to_normalize)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    normalized_data = scaler.fit_transform(df)
    
    # Create a DataFrame from the normalized data
    normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
    
    # Plot the normalized data
    fig, ax = plt.subplots()
    normalized_df.plot(ax=ax)
    ax.set_title('Normalized Data')
    ax.set_xlabel('Index')
    ax.set_ylabel('Normalized Value')
    
    return normalized_df, ax
data_dict = {
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [5, 4, 3, 2, 1],
    'feature3': [2, 3, 2, 3, 2]
}
data_keys = ['feature1', 'feature3']