
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data):
    # Check if the input data is a 2D array
    if not isinstance(data, pd.DataFrame) or data.ndim != 2:
        raise ValueError("Input data must be a 2D array.")
    
    # Check if the input data contains non-numeric data
    if not data.applymap(lambda x: isinstance(x, (int, float))).all().all():
        raise ValueError("Input data must contain only numeric values.")
    
    # Calculate the average of values across each row
    data['Average'] = data.mean(axis=1)
    
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
    
    # Create a heatmap of the correlations
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return data, heatmap