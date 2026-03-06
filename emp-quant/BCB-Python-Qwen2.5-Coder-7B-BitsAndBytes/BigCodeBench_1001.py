
import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path: str):
    # Read data from CSV file
    df = pd.read_csv(csv_file_path)
    
    # Normalize the 'column1'
    df['column1'] = (df['column1'] - df['column1'].min()) / (df['column1'].max() - df['column1'].min())
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(df.index, df['column1'], marker='o')
    
    # Set the title with formatted strings
    title = "{:<20}{:>20}".format('Plot Title', 'Normalized Column 1')
    ax.set_title(title)
    
    # Set the x-label with formatted strings
    xlabel = "{:<20}{:>20}".format('Index', 'Normalized Value')
    ax.set_xlabel(xlabel)
    
    # Set the y-label with formatted strings
    ylabel = "{:<20}{:>20}".format('Frequency', 'Normalized Value')
    ax.set_ylabel(ylabel)
    
    return ax