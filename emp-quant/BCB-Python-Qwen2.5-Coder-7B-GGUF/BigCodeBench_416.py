
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data, column="c"):
    """
    Removes a column from the given data dictionary and creates a heatmap of the correlation matrix of the remaining data.
    Non-numeric columns are excluded from the heatmap. If the data is empty or has no numeric columns, the function returns None.
    
    Parameters:
    data (dict): A dictionary where keys are column names and values are lists of data.
    column (str): The column name to be removed from the data.
    
    Returns:
    matplotlib.axes._axes.Axes or None: The Axes object of the heatmap or None if the heatmap is not generated.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Remove the specified column
    if column in df.columns:
        df = df.drop(columns=[column])
    
    # Check if the DataFrame is empty or has no numeric columns
    if df.empty or not df.select_dtypes(include=[np.number]).shape[1]:
        return None
    
    # Create a correlation matrix
    corr_matrix = df.corr()
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    
    # Return the Axes object of the heatmap
    return heatmap