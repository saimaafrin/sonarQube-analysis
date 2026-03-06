
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data):
    # Create a correlation matrix from the DataFrame
    corr = data.corr()

    # Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=np.bool))

    # Set up the matplotlib figure
    f, ax = plt.subplots(figsize=(11, 9))

    # Draw the heatmap with 'sns.heatmap()'
    sns.heatmap(corr, mask=mask, annot=True, cbar=False, square=True, cmap='coolwarm')

    # Set the title of the heatmap
    ax.set_title('Correlation Matrix')

    # Return the Axes object
    return ax