
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_dict):
    """
    Generates histograms for each column in the given DataFrame and checks if the value distributions are uniform.
    It prints a message for each non-uniform distribution.
    
    Parameters:
    data_dict (dict): A dictionary where keys are column names and values are lists of data points.
    
    Returns:
    List[plt.Axes]: A list of matplotlib Axes objects, each representing the histogram for a column.
    """
    # Convert the dictionary to a DataFrame
    df = pd.DataFrame(data_dict)
    
    # List to hold the Axes objects
    axes_list = []
    
    # Iterate over each column in the DataFrame
    for column in df.columns:
        # Create a histogram for the current column
        ax = df[column].hist(bins=20, figsize=(8, 6))
        axes_list.append(ax)
        
        # Check if the distribution is uniform
        if not df[column].nunique() == len(df[column]):
            print(f"Non-uniform distribution detected in column: {column}")
    
    return axes_list

axes = task_func(data_dict)
plt.show()