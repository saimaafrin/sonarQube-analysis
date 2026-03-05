import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(data, column="c"):
    """
    Removes a column from a given data dictionary and creates a heatmap of the correlation matrix of the remaining data.
    Non-numeric columns are excluded from the heatmap. If the data is empty or has no numeric columns, the function returns None.
    
    Parameters:
    - data (dict): A dictionary where keys are column names and values are lists of data points.
    - column (str): The column name to be removed from the data.
    
    Returns:
    - matplotlib.axes._axes.Axes or None: The Axes object of the heatmap or None if the heatmap is not generated.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Remove the specified column
    df = df.drop(columns=[column])
    
    # Filter out non-numeric columns
    df = df.select_dtypes(include=[float, int])
    
    # Check if the DataFrame is empty
    if df.empty:
        return None
    
    # Calculate the correlation matrix
    corr_matrix = df.corr()
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    
    # Return the Axes object of the heatmap
    return heatmap
data = {
    'a': [1, 2, 3, 4, 5],
    'b': [5, 4, 3, 2, 1],
    'c': ['x', 'y', 'z', 'w', 'v'],
    'd': [1.1, 2.2, 3.3, 4.4, 5.5]
}