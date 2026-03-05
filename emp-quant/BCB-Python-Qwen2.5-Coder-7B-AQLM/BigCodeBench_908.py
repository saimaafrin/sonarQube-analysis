
import os
import pandas as pd
import re
import matplotlib.pyplot as plt

def task_func(directory: str, pattern: str) -> list:
    # Initialize an empty list to store the Axes objects
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
            
            # Create a new figure and axis for each plot
            fig, ax = plt.subplots()
            
            # Plot the sales data with month on the x-axis and sales on the y-axis
            ax.plot(df['Month'], df['Sales'], marker='o')
            
            # Set the title of the plot to the filename
            ax.set_title(filename)
            
            # Append the Axes object to the list
            axes_list.append(ax)
    
    # Return the list of Axes objects
    return axes_list