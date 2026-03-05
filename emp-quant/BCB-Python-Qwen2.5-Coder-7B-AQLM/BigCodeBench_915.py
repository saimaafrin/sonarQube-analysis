
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

def task_func(df, z_threshold=2):
    """
    Identifies and plots outliers in the 'closing_price' column of a given DataFrame using the Z-Score method.
    
    Parameters:
    - df (pandas.DataFrame): The input DataFrame containing the 'closing_price' column.
    - z_threshold (float): The Z-Score threshold for identifying outliers. Default is 2.
    
    Returns:
    - tuple: A tuple containing the following elements:
        - pandas.DataFrame: A DataFrame containing the outliers in the 'closing_price' column.
        - matplotlib.axes._axes.Axes: The plot object displaying the outliers.
    """
    # Calculate the Z-Scores for the 'closing_price' column
    df['z_score'] = zscore(df['closing_price'])
    
    # Identify outliers based on the Z-Score threshold
    outliers = df[np.abs(df['z_score']) > z_threshold]
    
    # Plot the outliers
    fig, ax = plt.subplots()
    ax.scatter(df.index, df['closing_price'], color='blue', label='Data Points')
    ax.scatter(outliers.index, outliers['closing_price'], color='red', label='Outliers')
    ax.set_xlabel('Index')
    ax.set_ylabel('Closing Price')
    ax.set_title('Outliers in Closing Prices')
    ax.legend()
    
    return outliers, ax