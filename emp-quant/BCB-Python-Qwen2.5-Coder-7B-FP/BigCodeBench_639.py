import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(num_samples=100, num_features=5):
    """
    Generates a DataFrame with random values and calculates the correlation matrix.
    Visualizes the correlation matrix using a heatmap.

    Parameters:
    - num_samples: int, the number of samples in the DataFrame.
    - num_features: int, the number of features in the DataFrame.

    Returns:
    - DataFrame: The generated DataFrame with random values.
    - Axes: The heatmap visualization of the correlation matrix.
    """
    # Generate random data
    data = np.random.rand(num_samples, num_features)
    df = pd.DataFrame(data, columns=[f'Feature_{i+1}' for i in range(num_features)])
    
    # Calculate correlation matrix
    correlation_matrix = df.corr()
    
    # Visualize the correlation matrix using a heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return df, heatmap