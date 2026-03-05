
import numpy as np
import pandas as pd
import seaborn as sns

def task_func(num_samples=100, num_features=5):
    # Generate a random dataset with the specified number of samples and features
    data = np.random.rand(num_samples, num_features)
    # Create a Pandas DataFrame from the random data
    df = pd.DataFrame(data)
    # Calculate the correlation matrix
    corr_matrix = df.corr()
    # Visualize the correlation matrix as a heatmap
    sns.heatmap(corr_matrix, annot=True, cmap="viridis")
    return df, corr_matrix