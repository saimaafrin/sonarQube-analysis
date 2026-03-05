
import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

def task_func(df):
    # Replace NaN values with the average of the column
    df = df.fillna(df.mean())

    # Calculate statistics for each numeric column
    stats = df.describe()

    # Create a list of Axes objects to store the distribution plots
    axes = []

    # Loop through each numeric column and create a distribution plot
    for col in df.select_dtypes(np.number):
        # Calculate the histogram of the column
        hist = pd.Series(df[col].values).hist(bins=10)

        # Create a new Axes object to store the plot
        ax = plt.subplot(111)

        # Plot the histogram
        ax.hist(hist, bins=10)

        # Add a title to the plot
        ax.set_title(f"Distribution of {col}")

        # Add the Axes object to the list
        axes.append(ax)

    # Return the DataFrame with statistics and the list of Axes objects
    return df, axes