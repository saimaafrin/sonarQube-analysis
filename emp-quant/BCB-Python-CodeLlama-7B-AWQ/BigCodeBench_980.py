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
    if not df.select_dtypes(include=np.number).shape[1]:
        raise ValueError("No numeric columns present in the DataFrame.")

    # Standardize the numeric columns
    scaler = StandardScaler()
    df_std = scaler.fit_transform(df.select_dtypes(include=np.number))

    # Plot the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(df_std.corr(), annot=True, ax=ax)

    return df_std, fig
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})