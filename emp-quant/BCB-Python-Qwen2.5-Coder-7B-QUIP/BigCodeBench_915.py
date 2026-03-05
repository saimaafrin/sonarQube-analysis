
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

def task_func(df, z_threshold=2):
    # Calculate the Z-Score for the 'closing_price' column
    df['z_score'] = zscore(df['closing_price'])
    
    # Identify outliers based on the Z-Score threshold
    outliers = df[np.abs(df['z_score']) > z_threshold]
    
    # Plot the outliers
    fig, ax = plt.subplots()
    ax.plot(df.index, df['closing_price'], 'o', label='Closing Price')
    ax.plot(outliers.index, outliers['closing_price'], 'ro', label='Outlier')
    ax.set_xlabel('Index')
    ax.set_ylabel('Closing Price')
    ax.set_title('Outliers in Closing Prices')
    ax.legend()
    
    # Return the outliers DataFrame and the plot object
    return outliers, ax