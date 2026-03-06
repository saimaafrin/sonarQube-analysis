
import pandas as pd
import seaborn as sns

def task_func(array):
    # Check if the input array is empty or contains sublists of varying lengths
    if len(array) == 0 or len(array[0]) != 5:
        raise ValueError("Input array is empty or contains sublists of varying lengths")

    # Construct a DataFrame from the input 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])

    # Compute the correlation matrix of the DataFrame
    corr_matrix = df.corr()

    # Generate a seaborn heatmap of the correlation matrix
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm")

    # Return the DataFrame and the heatmap
    return df, sns.heatmap