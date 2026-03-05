import pandas as pd
import matplotlib.pyplot as plt
def task_func(csv_file_path: str):
    """
    This function reads data from a CSV file, normalizes a specific column named 'column1', and then plots the normalized data.
    """
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Normalize the data in the 'column1' column
    df['column1'] = df['column1'].apply(lambda x: x / df['column1'].max())

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(df['column1'])

    # Set the plot title
    title = f"Plot Title: {df.columns[0]}"
    ax.set_title(title, fontsize=14)

    # Set the x-label
    xlabel = f"Index: {df.index}"
    ax.set_xlabel(xlabel, fontsize=14)

    # Set the y-label
    ylabel = f"Frequency: {df['column1']}"
    ax.set_ylabel(ylabel, fontsize=14)

    return ax
csv_file_path = "data.csv"