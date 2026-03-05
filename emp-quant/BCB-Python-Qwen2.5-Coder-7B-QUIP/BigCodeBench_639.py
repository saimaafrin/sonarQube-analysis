
import numpy as np
import pandas as pd
import seaborn as sns
def task_func(num_samples=100, num_features=5):
    # Generate a DataFrame with random values
    data = pd.DataFrame(np.random.rand(num_samples, num_features), columns=[f"feature_{i}" for i in range(num_features)])
    
    # Calculate the correlation matrix
    correlation_matrix = data.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(8, 6))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt='%.2f')
    plt.title('Correlation Heatmap')
    plt.show()
    
    return data, heatmap