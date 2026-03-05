
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data):
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
    
    # Create a heatmap
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    
    # Set the title of the heatmap
    heatmap.set_title('Correlation Matrix')
    
    # Return the Axes object
    return heatmap