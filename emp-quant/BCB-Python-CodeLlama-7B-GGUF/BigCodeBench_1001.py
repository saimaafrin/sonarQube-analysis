
import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path: str):
    # Read data from CSV file
    df = pd.read_csv(csv_file_path)

    # Normalize column 'column1'
    df['column1_normalized'] = df['column1'] / df['column1'].max()

    # Create plot title
    title = f"Plot Title: {df.columns[0]} Normalized"

    # Create x-label
    xlabel = f"Index: {df.index.name}"

    # Create y-label
    ylabel = f"Frequency: {df.columns[1]} Normalized"

    # Plot data
    ax = df.plot(kind='bar', x=df.index, y='column1_normalized', title=title, xlabel=xlabel, ylabel=ylabel)

    return ax