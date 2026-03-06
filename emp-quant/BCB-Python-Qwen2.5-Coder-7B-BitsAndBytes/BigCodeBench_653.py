
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def task_func(dataframe, target_value='332'):
    # Create a DataFrame to store the boolean results
    bool_df = dataframe == target_value
    
    # Create a heatmap using seaborn
    ax = sns.heatmap(bool_df, cmap='Greens', cbar=False)
    
    # Set the title of the plot
    ax.set_title(f'Occurrences of {target_value} in the DataFrame')
    
    # Return the boolean DataFrame and the Axes object
    return bool_df, ax