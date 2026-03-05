
import pandas as pd
import seaborn as sns

def task_func(array):
    # Check if the input array is empty or contains sublists of varying lengths
    if not array or len(array[0]) != 5:
        raise ValueError("Input array is empty or contains sublists of varying lengths")

    # Create a DataFrame from the input 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])

    # Create a seaborn heatmap of the DataFrame's correlation matrix
    heatmap = sns.heatmap(df.corr(), annot=True, cmap="coolwarm")

    return df, heatmap