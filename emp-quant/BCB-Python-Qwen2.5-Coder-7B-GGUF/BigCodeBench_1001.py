
import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path: str):
    # Read data from CSV file
    data = pd.read_csv(csv_file_path)
    
    # Normalize the 'column1'
    data['column1'] = (data['column1'] - data['column1'].min()) / (data['column1'].max() - data['column1'].min())
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(data['column1'], label='Normalized Column 1')
    
    # Set the title with formatted string
    ax.set_title(f"{'Plot Title':<20}:{'Normalized Column 1':>20}")
    
    # Set the x-label with formatted string
    ax.set_xlabel(f"{'Index':<20}:{'Normalized Value':>20}")
    
    # Set the y-label with formatted string
    ax.set_ylabel(f"{'Frequency':<20}:{'Normalized Value':>20}")
    
    # Show legend
    ax.legend()
    
    # Return the Axes object
    return ax