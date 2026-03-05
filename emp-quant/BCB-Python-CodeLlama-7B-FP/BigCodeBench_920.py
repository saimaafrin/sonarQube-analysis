import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(data):
    """
    Draw and return a correlation matrix heatmap for a DataFrame containing numerical columns.
    The title of the heatmap is set to 'Correlation Matrix'.
    """
    # Check if the input is a DataFrame
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Check if the DataFrame contains only numerical columns
    if not all(data.dtypes == "float64"):
        raise ValueError("DataFrame must contain only numerical columns")

    # Create a correlation matrix
    corr = data.corr()

    # Draw a heatmap of the correlation matrix
    ax = sns.heatmap(corr, annot=True, cmap="coolwarm", cbar=False)

    # Set the title of the heatmap
    ax.set_title("Correlation Matrix")

    # Return the Axes object representing the heatmap
    return ax
data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})