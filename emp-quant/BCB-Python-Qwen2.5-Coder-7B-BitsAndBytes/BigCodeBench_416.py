
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data, column="c"):
    """
    Removes a specified column from the data dictionary and creates a heatmap of the 
    correlation matrix of the remaining data. Non-numeric columns are excluded.

    Parameters:
    - data (dict): A dictionary where keys are column names and values are lists of data points.
    - column (str): The name of the column to be removed.

    Returns:
    - matplotlib.axes._axes.Axes or None: The Axes object of the heatmap or None if the heatmap is not generated.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data)
    
    # Drop the specified column
    df.drop(columns=[column], inplace=True)
    
    # Filter out non-numeric columns
    df_numeric = df.select_dtypes(include=[float, int])
    
    # Check if there are any numeric columns left
    if df_numeric.empty:
        return None
    
    # Calculate the correlation matrix
    corr_matrix = df_numeric.corr()
    
    # Create a heatmap of the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', linewidths=0.5, ax=ax)
    
    return ax