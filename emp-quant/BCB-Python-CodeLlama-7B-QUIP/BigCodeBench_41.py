
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew

def task_func(data_matrix):
    # Calculate the skewness of each row
    skewness = data_matrix.apply(skew, axis=1)

    # Create a new column with the skewness
    skewness_df = pd.DataFrame(skewness, columns=['Skewness'])

    # Plot the distribution of the skewness
    fig, ax = plt.subplots()
    ax.hist(skewness_df['Skewness'], bins=50)
    ax.set_xlabel('Skewness')
    ax.set_ylabel('Count')
    ax.set_title('Skewness Distribution')
    plt.show()

    return skewness_df