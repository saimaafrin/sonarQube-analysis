
import pandas as pd
import seaborn as sns
def task_func(array):
    # Check if the input array is empty or contains sublists of varying lengths
    if len(array) == 0 or len(array[0]) != 5:
        raise ValueError("Input array is empty or contains sublists of varying lengths")

    # Construct the DataFrame
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])

    # Compute the correlation matrix
    corr_matrix = df.corr()

    # Generate the heatmap
    heatmap = sns.heatmap(corr_matrix, annot=True, cmap="viridis")

    return df, heatmap