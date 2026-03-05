import pandas as pd
import seaborn as sns
def task_func(data):
    """
    Analyze a dataset by calculating the average of values across each row and visualizing the correlation matrix as a heatmap.
    The function should raise the exception for: ValueError: If the input data is not a 2D array or if it contains non-numeric data.
    The function should output with:
        tuple: A tuple containing:
            DataFrame: A pandas DataFrame enhanced with an 'Average' column that represents the mean across each row.
            Axes: The matplotlib Axes object showing the heatmap of the correlations.
    """
    # Check if the input data is a 2D array
    if not isinstance(data, np.ndarray) or data.ndim != 2:
        raise ValueError("Input data must be a 2D array")

    # Check if the input data contains non-numeric data
    if not np.issubdtype(data.dtype, np.number):
        raise ValueError("Input data must contain only numeric values")

    # Calculate the average of values across each row
    data["Average"] = data.mean(axis=1)

    # Create a heatmap of the correlations
    sns.heatmap(data.corr(), annot=True, cmap="coolwarm")

    # Return the DataFrame and the Axes object
    return data, sns.heatmap.axes
data = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})