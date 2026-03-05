
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew

def task_func(data_matrix):
    # Calculate the skewness of each row
    skewness_values = data_matrix.skew(axis=1)
    
    # Create a DataFrame to store the skewness values
    skewness_df = pd.DataFrame(skewness_values, columns=['Skewness'])
    
    # Plot the distribution of the skewness values
    fig, ax = plt.subplots()
    skewness_df['Skewness'].plot(kind='hist', ax=ax, bins=30, color='blue', edgecolor='black')
    ax.set_title('Distribution of Row Skewness')
    ax.set_xlabel('Skewness')
    ax.set_ylabel('Frequency')
    
    return skewness_df, ax