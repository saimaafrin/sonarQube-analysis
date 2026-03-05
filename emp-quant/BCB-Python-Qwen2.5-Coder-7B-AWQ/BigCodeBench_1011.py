import pandas as pd
import matplotlib.pyplot as plt
def task_func(csv_file_path, col1_name="column1", col2_name="column2"):
    # Read data from the CSV file
    df = pd.read_csv(csv_file_path)
    
    # Group the DataFrame by col1_name and calculate the mean of col2_name for each group
    grouped_data = df.groupby(col1_name)[col2_name].mean().reset_index()
    
    # Create a bar plot
    ax = grouped_data.plot(kind='bar', x=col1_name, y=col2_name, legend=False)
    
    # Set the title and axis labels
    ax.set_title(f"Mean of {col2_name} Grouped by {col1_name}")
    ax.set_xlabel(col1_name)
    ax.set_ylabel(f"Mean of {col2_name}")
    
    # Return the Axes object
    return ax