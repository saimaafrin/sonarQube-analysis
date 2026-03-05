
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(data):
    """
    Normalizes a given dataset using MinMax scaling and calculates the average of each row.
    This average is then added as a new column 'Average' to the resulting DataFrame.
    The function also visualizes these averages in a plot.

    Parameters:
    data (pd.DataFrame): The input DataFrame to be normalized and averaged.

    Returns:
    pd.DataFrame: A pandas DataFrame with normalized data and an additional 'Average' column.
    Axes: A matplotlib Axes object showing a bar subplot of the average values.
    """
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Normalize the data
    normalized_data = scaler.fit_transform(data)
    
    # Convert the normalized data back to a DataFrame
    normalized_df = pd.DataFrame(normalized_data, columns=data.columns)
    
    # Calculate the average of each row
    normalized_df['Average'] = normalized_df.mean(axis=1)
    
    # Plot the average values
    fig, ax = plt.subplots()
    ax.bar(range(len(normalized_df)), normalized_df['Average'])
    ax.set_xlabel('Row Index')
    ax.set_ylabel('Average Value')
    ax.set_title('Average Values of Rows')
    
    return normalized_df, ax