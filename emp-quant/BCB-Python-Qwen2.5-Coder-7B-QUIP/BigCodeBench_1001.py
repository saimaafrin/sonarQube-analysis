
import pandas as pd
import matplotlib.pyplot as plt

def task_func(csv_file_path: str):
    # Read data from CSV
    data = pd.read_csv(csv_file_path)
    
    # Normalize the 'column1' column
    data['column1'] = data['column1'] / data['column1'].max()
    
    # Create the plot
    fig, ax = plt.subplots()
    ax.plot(data['column1'], 'b-')
    
    # Set the title with formatted string
    title = f"{'Plot Title':<20}:{'Normalized Column 1':<20}"
    ax.set_title(title)
    
    # Set the x-label with formatted string
    x_label = f"{'Index':<20}:{'Normalized Value':<20}"
    ax.set_xlabel(x_label)
    
    # Set the y-label with formatted string
    y_label = f"{'Frequency':<20}:{'Normalized Value':<20}"
    ax.set_ylabel(y_label)
    
    # Return the plot
    return ax