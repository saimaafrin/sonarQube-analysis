
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

def task_func(df, z_threshold=2):
    # Calculate the Z-Scores for the 'closing_price' column
    z_scores = np.abs(zscore(df['closing_price']))
    
    # Identify outliers based on the Z-Score threshold
    outliers = df[z_scores > z_threshold]
    
    # Plotting the outliers
    fig, ax = plt.subplots()
    ax.scatter(outliers.index, outliers['closing_price'], color='red')
    ax.set_xlabel('Index')
    ax.set_ylabel('Closing Price')
    ax.set_title('Outliers in Closing Prices')
    
    return outliers, ax