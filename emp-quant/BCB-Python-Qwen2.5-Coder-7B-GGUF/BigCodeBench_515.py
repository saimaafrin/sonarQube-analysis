
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(array):
    if not array or any(len(sublist) != 5 for sublist in array):
        raise ValueError("Input array must not be empty and all sublists must have length 5.")
    
    # Create DataFrame from the 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])
    
    # Calculate the correlation matrix
    correlation_matrix = df.corr()
    
    # Create a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', linewidths=0.5)
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return df, correlation_matrix

df, correlation_matrix = task_func(array)
print(df)
print(correlation_matrix)