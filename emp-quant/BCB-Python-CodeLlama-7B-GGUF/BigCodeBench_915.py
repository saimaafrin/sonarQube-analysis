
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

def task_func(df, z_threshold=2):
    # Calculate the Z-scores for the 'closing_price' column
    z_scores = zscore(df['closing_price'])
    
    # Identify outliers based on the Z-scores
    outliers = df[np.abs(z_scores) > z_threshold]
    
    # Create a plot of the outliers
    fig, ax = plt.subplots()
    ax.plot(df.index, df['closing_price'], 'bo-')
    ax.set_xlabel('Index')
    ax.set_ylabel('Closing Price')
    ax.set_title('Outliers in Closing Prices')
    ax.set_facecolor('lightgray')
    ax.grid(True)
    
    return outliers, ax