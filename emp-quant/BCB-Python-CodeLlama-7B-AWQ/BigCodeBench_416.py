import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
def task_func(data, column="c"):
    """
    Removes a column from a given data dictionary and creates a heatmap of the correlation matrix of the remaining data. Non-numeric columns are excluded from the heatmap. If the data is empty or has no numeric columns, the function returns None.
    """
    # Check if the data is empty or has no numeric columns
    if data.empty or not data.select_dtypes(include=[np.number]).shape[1]:
        return None

    # Remove the specified column from the data
    data = data.drop(columns=[column])

    # Create a correlation matrix of the remaining data
    corr = data.corr()

    # Create a heatmap of the correlation matrix
    sns.heatmap(corr, annot=True, cmap="coolwarm")

    # Return the Axes object of the heatmap
    return plt.gca()
data = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6], "c": [7, 8, 9]})