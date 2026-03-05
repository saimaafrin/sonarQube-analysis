
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data):
    # Check if the input data is a 2D array
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a 2D array (DataFrame).")
    
    # Check if the data contains non-numeric data
    if not data.select_dtypes(include=[float, int]).notnull().all().all():
        raise ValueError("Input data must contain only numeric values.")
    
    # Calculate the average of values across each row
    data['Average'] = data.mean(axis=1)
    
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    
    # Return the DataFrame with the 'Average' column and the heatmap
    return data, heatmap