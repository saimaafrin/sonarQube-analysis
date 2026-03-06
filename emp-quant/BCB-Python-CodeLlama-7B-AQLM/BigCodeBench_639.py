import numpy as np
import pandas as pd
import seaborn as sns
def task_func(num_samples=100, num_features=5):
    """
    Generate a Pandas DataFrame with random values, representing a dataset with multiple features. 
    Calculate the correlation between the features and visualize this information using a heatmap.
    
    Parameters:
    - num_samples (int): The number of samples to generate. Default is 100.
    - num_features (int): The number of features to generate. Default is 5.
    
    Returns:
    - DataFrame: The generated DataFrame with random values.
    - Axes: The heatmap visualization of the correlation matrix.

    Requirements:
    - pandas
    - numpy
    - seaborn
    
    Example:
    >>> df, ax = task_func(10, 3)
    >>> ax.figure.show()
    """
    df = pd.DataFrame(np.random.randn(num_samples, num_features), columns=['f' + str(i) for i in range(num_features)])
    corr = df.corr()
    ax = sns.heatmap(corr, cmap='coolwarm', square=True, linewidths=0.5, cbar=True, annot=True, fmt='.2f', annot_kws={'size': 10})
    return df, ax