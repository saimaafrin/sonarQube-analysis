import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(num_samples=100, num_features=5):
    # Generate a DataFrame with random values
    data = np.random.rand(num_samples, num_features)
    columns = [f'Feature_{i+1}' for i in range(num_features)]
    df = pd.DataFrame(data, columns=columns)
    
    # Calculate the correlation between the features
    correlation_matrix = df.corr()
    
    # Visualize the correlation matrix using a heatmap
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Heatmap')
    plt.show()
    
    return df, heatmap