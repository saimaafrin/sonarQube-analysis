
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data, column="c"):
    # Remove the specified column from the data
    if column in data.columns:
        data = data.drop(columns=[column])
    
    # Filter out non-numeric columns
    numeric_data = data.select_dtypes(include=[float, int])
    
    # Check if there are any numeric columns left
    if numeric_data.empty:
        return None
    
    # Calculate the correlation matrix
    correlation_matrix = numeric_data.corr()
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    
    # Return the Axes object of the heatmap
    return heatmap