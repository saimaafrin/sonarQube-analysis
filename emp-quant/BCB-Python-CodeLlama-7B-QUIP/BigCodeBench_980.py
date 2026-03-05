
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

def task_func(df):
    # Check if the DataFrame is empty
    if df.empty:
        raise ValueError("The DataFrame is empty")

    # Get the numeric columns
    numeric_columns = df.select_dtypes(np.number)

    # Check if there are any numeric columns
    if len(numeric_columns) == 0:
        raise ValueError("No numeric columns present in the DataFrame")

    # Standardize the numeric columns
    scaler = StandardScaler()
    standardized_df = scaler.fit_transform(numeric_columns)

    # Create a correlation matrix
    correlation_matrix = np.corrcoef(standardized_df)

    # Plot the correlation matrix
    fig, ax = plt.subplots(figsize=(8, 8))
    sns.heatmap(correlation_matrix, ax=ax, cmap="coolwarm")
    ax.set_xticks(np.arange(len(standardized_df.columns)) + 0.5, minor=True)
    ax.set_yticks(np.arange(len(standardized_df.columns)) + 0.5, minor=True)
    ax.grid(which="minor")
    ax.grid(which="major")
    ax.set_aspect("equal")
    plt.show()

    return standardized_df, fig