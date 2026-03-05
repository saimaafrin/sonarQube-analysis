import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
def task_func(df):
    """
    Plots the correlation matrix from numeric columns in a DataFrame and returns a DataFrame where the numeric columns are standardized to have mean 0 and variance 1.
    """
    # Check if the DataFrame is empty or if no numeric columns are present
    if df.empty or not df.select_dtypes(include=[np.number]).shape[1]:
        raise ValueError("The DataFrame is empty or no numeric columns are present.")

    # Create a correlation matrix from the numeric columns
    corr_matrix = df.select_dtypes(include=[np.number]).corr()

    # Plot the correlation matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", ax=ax)

    # Standardize the numeric columns
    scaler = StandardScaler()
    scaled_df = scaler.fit_transform(df.select_dtypes(include=[np.number]))

    return scaled_df, fig
df = pd.DataFrame({"A": [1, 2, 3], "B": [4, 5, 6], "C": [7, 8, 9]})