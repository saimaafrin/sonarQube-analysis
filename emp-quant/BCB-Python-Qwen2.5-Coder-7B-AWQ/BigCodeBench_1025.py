import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
PLOT_TITLE = "Scaled Values"
def task_func(data_dict):
    """
    Scales the values in a given dictionary using MinMaxScaler and plots the scaled data.
    
    Parameters:
    data_dict (dict): A dictionary where keys are feature names and values are lists of feature values.
    
    Returns:
    pandas.DataFrame: A DataFrame containing the scaled data.
    matplotlib.Axes: An Axes object that displays the plot of the scaled data.
    """
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(data_dict)
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df)
    
    # Convert the scaled data back to a DataFrame
    scaled_df = pd.DataFrame(scaled_data, columns=df.columns)
    
    # Plot the scaled data
    fig, ax = plt.subplots()
    ax.plot(scaled_df)
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel('Features')
    ax.set_ylabel('Scaled Values')
    
    return scaled_df, ax