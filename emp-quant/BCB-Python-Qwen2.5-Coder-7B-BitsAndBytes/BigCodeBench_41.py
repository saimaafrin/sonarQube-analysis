
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew

def task_func(data_matrix):
    # Convert the input data to a pandas DataFrame
    df = pd.DataFrame(data_matrix)
    
    # Calculate the skewness for each row
    df['Skewness'] = df.apply(lambda row: skew(row), axis=1)
    
    # Plot the distribution of skewness values
    fig, ax = plt.subplots()
    df['Skewness'].plot(kind='hist', bins=30, ax=ax)
    ax.set_title('Distribution of Row Skewness')
    ax.set_xlabel('Skewness')
    ax.set_ylabel('Frequency')
    
    return df, ax