import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def task_func(df):
    """
    Plots the correlation matrix from numeric columns in a DataFrame and returns a DataFrame where the numeric columns are standardized to have mean 0 and variance 1.
    Notes:
        - Only numeric columns are considered for the heatmap.
        - Non-numeric columns are ignored.
        - The function should raise the exception for:
            - ValueError: If the DataFrame is empty or if no numeric columns are present.
        - The function should output with:
            - pandas.DataFrame: Standardized DataFrame.
            - matplotlib.figure.Figure: Figure object containing the heatmap of the correlation matrix.
    """
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty.")

    # Check if there are any numeric columns
    numeric_columns = df.select_dtypes(include=np.number).columns
    if not numeric_columns:
        raise ValueError("No numeric columns present in the DataFrame.")

    # Standardize the numeric columns
    scaler = StandardScaler()
    standardized_df = scaler.fit_transform(df[numeric_columns])

    # Plot the correlation matrix
    heatmap = sns.heatmap(standardized_df.corr(), annot=True, cmap="coolwarm")

    # Return the standardized DataFrame and the heatmap
    return standardized_df, heatmap
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})