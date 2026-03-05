
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(csv_file_path: str, title: str):
    # Load the CSV file
    df = pd.read_csv(csv_file_file_path)

    # Compute the correlation matrix
    corr_matrix = df.corr()

    # Round the correlation values to 2 decimals
    corr_matrix = corr_matrix.round(2)

    # Create a heatmap from the correlation matrix
    sns.heatmap(corr_matrix, annot=True, cmap="viridis")

    # Set the title of the plot
    plt.title(title)

    # Show the plot
    plt.show()

    # Return the Axes object of the plot
    return plt.gca()