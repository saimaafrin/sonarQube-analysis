import os
import pandas as pd
import re
import matplotlib.pyplot as plt
def task_func(directory: str, pattern: str) -> list:
    # List to hold the axes objects
    axes_list = []
    
    # Compile the regular expression pattern
    regex = re.compile(pattern)
    
    # Walk through the directory
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file matches the pattern
            if regex.match(file):
                # Construct the full file path
                file_path = os.path.join(root, file)
                
                # Read the CSV file into a DataFrame
                df = pd.read_csv(file_path)
                
                # Create a plot for the sales data
                fig, ax = plt.subplots()
                ax.plot(df['Month'], df['Sales'], marker='o')
                ax.set_xlabel('Month')
                ax.set_ylabel('Sales')
                ax.set_title(f'Sales Data from {file}')
                
                # Append the axes object to the list
                axes_list.append(ax)
    
    return axes_list