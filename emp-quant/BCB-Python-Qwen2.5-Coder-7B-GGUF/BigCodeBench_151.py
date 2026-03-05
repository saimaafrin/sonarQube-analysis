
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data_dict, data_keys):
    # Check if any of the keys are in the data_dict
    if not any(key in data_dict for key in data_keys):
        raise ValueError("No keys in `data_keys` are found in `data_dict`.")
    
    # Extract the data for the specified keys
    data_to_scale = {key: data_dict[key] for key in data_keys if key in data_dict}
    
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_to_scale)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    normalized_data = scaler.fit_transform(df)
    
    # Convert the normalized data back to a DataFrame
    normalized_df = pd.DataFrame(normalized_data, columns=df.columns)
    
    # Plot the normalized data
    fig, ax = plt.subplots()
    normalized_df.plot(ax=ax)
    ax.set_title('Normalized Data')
    ax.set_xlabel('Data Points')
    ax.set_ylabel('Normalized Values')
    
    return normalized_df, ax