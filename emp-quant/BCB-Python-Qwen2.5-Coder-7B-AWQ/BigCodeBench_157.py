import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(data):
    """
    Analyzes a dataset by calculating the average of values across each row and visualizing the correlation matrix as a heatmap.
    
    Parameters:
    data (pd.DataFrame): A 2D pandas DataFrame containing numeric data.
    
    Returns:
    tuple: A tuple containing:
        DataFrame: A pandas DataFrame enhanced with an 'Average' column that represents the mean across each row.
        Axes: The matplotlib Axes object showing the heatmap of the correlations.
    """
    # Check if the input data is a 2D array
    if not isinstance(data, pd.DataFrame) or data.ndim != 2:
        raise ValueError("Input data must be a 2D pandas DataFrame.")
    
    # Check if the data contains non-numeric data
    if not data.apply(pd.to_numeric, errors='coerce').notnull().all().all():
        raise ValueError("Input data must contain only numeric values.")
    
    # Calculate the average of values across each row
    data['Average'] = data.mean(axis=1)
    
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
    
    # Visualize the correlation matrix as a heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return data, heatmap