import pandas as pd
import matplotlib.pyplot as plt
def task_func(csv_file_path: str):
    # Read data from CSV file
    df = pd.read_csv(csv_file_path)

    # Normalize column
    df['column1'] = (df['column1'] - df['column1'].mean()) / df['column1'].std()

    # Plot normalized data
    fig, ax = plt.subplots()
    ax.plot(df['column1'])

    # Set plot title
    ax.set_title(f'Plot Title: {df.columns[0]}')

    # Set x-label
    ax.set_xlabel(f'Index: {df.index}')

    # Set y-label
    ax.set_ylabel(f'Frequency: {df["column1"]}')

    return ax
csv_file_path = 'data.csv'
df = pd.read_csv(csv_file_path)