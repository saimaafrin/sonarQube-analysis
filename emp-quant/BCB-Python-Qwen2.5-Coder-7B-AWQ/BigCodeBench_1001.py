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
    
    # Format the title
    title = '{:<20}{:>20}'.format('Plot Title', 'Normalized Column 1')
    ax.set_title(title)
    
    # Format the x-label
    x_label = '{:<20}{:>20}'.format('Index', 'Normalized Value')
    ax.set_xlabel(x_label)
    
    # Format the y-label
    y_label = '{:<20}{:>20}'.format('Frequency', 'Normalized Value')
    ax.set_ylabel(y_label)
    
    # Return the Axes object
    return ax