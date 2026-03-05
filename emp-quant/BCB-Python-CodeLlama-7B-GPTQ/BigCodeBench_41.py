import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
def task_func(data_matrix):
    # Calculate the skewness of each row in the data matrix
    skewness = data_matrix.apply(skew, axis=1)

    # Create a new column in the DataFrame with the skewness values
    skewness_df = pd.DataFrame(skewness, columns=['Skewness'])

    # Plot the distribution of the skewness values
    ax = skewness_df['Skewness'].plot(kind='hist', bins=20)

    # Return the DataFrame and the Axes object
    return skewness_df, ax
data_matrix = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]])