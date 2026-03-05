
import pandas as pd
import seaborn as sns

def task_func(data):
    # Create a correlation matrix from the DataFrame
    corr_matrix = data.corr()

    # Generate a heatmap from the correlation matrix
    sns.heatmap(corr_matrix, annot=True, cmap="coolwarm", cbar=False, xticklabels=data.columns, yticklabels=data.columns)

    # Set the title of the heatmap
    plt.title("Correlation Matrix")

    # Return the Axes object representing the heatmap
    return plt.gca()