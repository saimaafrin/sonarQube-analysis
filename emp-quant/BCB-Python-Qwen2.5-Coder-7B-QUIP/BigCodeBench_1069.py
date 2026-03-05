
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data_dict):
    # Create a list to store the Axes objects
    axes_list = []
    
    # Iterate over each column in the DataFrame
    for column_name in data_dict:
        # Create a histogram for the column
        fig, ax = plt.subplots()
        data_dict[column_name].hist(ax=ax)
        axes_list.append(ax)
        
        # Check if the distribution is uniform
        if not is_uniform_distribution(data_dict[column_name]):
            print(f"Non-uniform distribution detected in column: {column_name}")
    
    return axes_list

def is_uniform_distribution(series):
    # This is a simple check to determine if the distribution is uniform
    # In a real scenario, you might need a more sophisticated method
    return series.std() / series.mean() < 0.1