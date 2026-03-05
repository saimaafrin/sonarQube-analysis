
import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path: str):
    # Read the CSV file
    df = pd.read_csv(csv_file_path)

    # Normalize the 'column1' column
    df['column1'] = df['column1'] / df['column1'].max()

    # Set the plot title
    plt.title('Plot Title: Normalized Column 1')

    # Set the x-label and y-label
    plt.xlabel('Index: Normalized Value')
    plt.ylabel('Frequency: Normalized Value')

    # Plot the normalized data
    plt.plot(df['column1'])

    # Return the matplotlib.axes.Axes object
    return plt.gca()