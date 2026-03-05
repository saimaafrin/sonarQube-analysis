import numpy as np
import pandas as pd
import seaborn as sns
def task_func(num_samples=100, num_features=5):
    """
    Generate a Pandas DataFrame with random values, representing a dataset with multiple features.
    Calculate the correlation between the features and visualize this information using a heatmap.
    """
    # Generate random data
    data = np.random.rand(num_samples, num_features)

    # Create a Pandas DataFrame
    df = pd.DataFrame(data, columns=['feature_%d' % i for i in range(num_features)])

    # Calculate the correlation matrix
    corr = df.corr()

    # Visualize the correlation matrix using a heatmap
    sns.heatmap(corr, annot=True, cmap='coolwarm')

    return df, corr