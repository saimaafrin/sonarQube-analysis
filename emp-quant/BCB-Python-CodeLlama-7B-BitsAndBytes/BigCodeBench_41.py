
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew

def task_func(data_matrix):
    # Calculate the skewness of each row in the data matrix
    skewness = data_matrix.apply(skew, axis=1)

    # Create a new column in the DataFrame with the skewness values
    skewness_df = pd.DataFrame(skewness, columns=['Skewness'])

    # Plot the distribution of the skewness values
    ax = skewness_df['Skewness'].plot(kind='hist', bins=50)

    # Add a title and labels to the plot
    ax.set_title('Skewness Distribution')
    ax.set_xlabel('Skewness')
    ax.set_ylabel('Frequency')

    return skewness_df, ax