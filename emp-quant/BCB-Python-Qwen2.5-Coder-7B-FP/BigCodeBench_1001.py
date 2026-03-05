import pandas as pd
import matplotlib.pyplot as plt
def task_func(csv_file_path: str):
    # Read data from CSV file
    data = pd.read_csv(csv_file_path)
    
    # Normalize the 'column1'
    data['column1'] = (data['column1'] - data['column1'].min()) / (data['column1'].max() - data['column1'].min())
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(data['column1'], 'b-')
    
    # Set the title with formatted string
    ax.set_title('{:<20}{:>20}'.format('Plot Title', 'Normalized Column 1'))
    
    # Set the x-label with formatted string
    ax.set_xlabel('{:<20}{:>20}'.format('Index', 'Normalized Value'))
    
    # Set the y-label with formatted string
    ax.set_ylabel('{:<20}{:>20}'.format('Frequency', 'Normalized Value'))
    
    # Return the Axes object
    return ax