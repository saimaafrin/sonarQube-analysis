
import pandas as pd
import seaborn as sns

def task_func(array):
    # Check if the input array is empty
    if not array or len(array) == 0:
        raise ValueError("Input array is empty")
    
    # Check if all sublists have the same length
    if not all(len(sublist) == 5 for sublist in array):
        raise ValueError("Sublists must be of length 5")
    
    # Construct the DataFrame
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])
    
    # Calculate the correlation matrix
    corr_matrix = df.corr()
    
    # Plot the heatmap
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm')
    plt.show()
    
    return df, corr_matrix