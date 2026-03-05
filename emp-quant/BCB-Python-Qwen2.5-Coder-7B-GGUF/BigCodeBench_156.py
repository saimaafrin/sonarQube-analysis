
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    """
    Normalizes the given dataset using MinMax scaling and calculates the average of each row.
    Adds the average as a new column 'Average' to the resulting DataFrame and plots these averages.
    
    Parameters:
    data (pd.DataFrame): The input DataFrame to be normalized and processed.
    
    Returns:
    pd.DataFrame: The processed DataFrame with an additional 'Average' column.
    matplotlib.axes._subplots.AxesSubplot: The Axes object of the bar plot.
    """
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Normalize the data
    normalized_data = scaler.fit_transform(data)
    
    # Convert the normalized data back to DataFrame
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns)
    
    # Calculate the average of each row
    normalized_df['Average'] = normalized_df.mean(axis=1)
    
    # Plotting the averages
    fig, ax = plt.subplots()
    ax.bar(range(len(normalized_df)), normalized_df['Average'], color='skyblue')
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Average Value')
    ax.set_title('Average Values of Rows in Normalized Dataset')
    
    return normalized_df, ax