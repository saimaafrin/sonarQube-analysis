import pandas as pd
import seaborn as sns
def task_func(data):
    """
    Draw and return a correlation matrix heatmap for a DataFrame containing numerical columns.
    The title of the heatmap is set to 'Correlation Matrix'.
    """
    # Create a correlation matrix from the DataFrame
    corr = data.corr()

    # Generate a heatmap from the correlation matrix
    ax = sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", xticklabels=data.columns, yticklabels=data.columns)

    # Set the title of the heatmap
    ax.set_title("Correlation Matrix")

    return ax
data = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [2, 4, 6, 8, 10], "C": [3, 6, 9, 12, 15]})