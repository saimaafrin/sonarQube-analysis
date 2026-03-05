
import numpy as np
import pandas as pd
import seaborn as sns

def task_func(num_samples=100, num_features=5):
    # Generate random data
    data = np.random.rand(num_samples, num_features)
    # Create a Pandas DataFrame
    df = pd.DataFrame(data, columns=['Feature ' + str(i) for i in range(num_features)])
    # Calculate correlation matrix
    corr_matrix = df.corr()
    # Visualize correlation matrix as a heatmap
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    return df, corr_matrix