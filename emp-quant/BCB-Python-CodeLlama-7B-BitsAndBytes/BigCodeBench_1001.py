
import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path: str):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Normalize the 'column1' column
    df['column1_normalized'] = df['column1'] / df['column1'].max()

    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(df['column1_normalized'])

    # Set the plot title
    title = f"Plot Title: {df.columns[0]}"
    ax.set_title(title, fontsize=20)

    # Set the x-label
    xlabel = f"Index: {df.index}"
    ax.set_xlabel(xlabel, fontsize=20)

    # Set the y-label
    ylabel = f"Frequency: {df['column1_normalized']}"
    ax.set_ylabel(ylabel, fontsize=20)

    # Show the plot
    plt.show()

    return ax