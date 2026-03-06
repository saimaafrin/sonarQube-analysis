
import pandas as pd
import seaborn as sns

def task_func(data, column="c"):
    # Remove the specified column from the data
    data = data.drop(columns=[column])

    # Check if the data has any numeric columns
    if data.select_dtypes(include=[np.number]).shape[1] == 0:
        return None

    # Create a correlation matrix of the remaining data
    corr = data.corr()

    # Create a heatmap of the correlation matrix
    ax = sns.heatmap(corr, annot=True, cmap="coolwarm")

    return ax