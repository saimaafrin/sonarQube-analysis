
import pandas as pd
import seaborn as sns

def task_func(data, column="c"):
    # Check if the data is empty or has no numeric columns
    if data.empty or not data.select_dtypes(include=['number']).any():
        return None

    # Remove the specified column from the data
    data = data.drop(columns=[column])

    # Calculate the correlation matrix
    corr_matrix = data.corr()

    # Create a heatmap of the correlation matrix
    heatmap = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')

    # Return the Axes object of the heatmap
    return heatmap