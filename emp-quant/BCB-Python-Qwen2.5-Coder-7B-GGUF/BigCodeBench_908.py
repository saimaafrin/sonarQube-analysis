
import os
import pandas as pd
import re
import matplotlib.pyplot as plt

def task_func(directory: str, pattern: str) -> list:
    # List to hold the axes objects
    axes_list = []
    
    # Compile the regular expression pattern
    regex = re.compile(pattern)
    
    # Iterate over all files in the directory
    for filename in os.listdir(directory):
        # Check if the file matches the pattern
        if regex.match(filename):
            # Construct the full file path
            file_path = os.path.join(directory, filename)
            
            # Read the CSV file into a pandas DataFrame
            df = pd.read_csv(file_path)
            
            # Create a new figure and axis
            fig, ax = plt.subplots()
            
            # Plot the sales data
            ax.plot(df['Month'], df['Sales'], marker='o')
            
            # Set the title and labels
            ax.set_title(f'Sales Data from {filename}')
            ax.set_xlabel('Month')
            ax.set_ylabel('Sales')
            
            # Append the axis object to the list
            axes_list.append(ax)
    
    # Return the list of axes objects
    return axes_list