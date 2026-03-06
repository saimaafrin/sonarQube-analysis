
import pandas as pd
import seaborn as sns

def task_func(array):
    if not array or any(len(sublist) != 5 for sublist in array):
        raise ValueError("Input array must be non-empty and contain sublists of length 5.")
    
    # Create DataFrame from the 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])
    
    # Calculate the correlation matrix
    corr_matrix = df.corr()
    
    # Generate the heatmap
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.show()
    
    return df, corr_matrix