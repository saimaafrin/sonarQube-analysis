
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def task_func(dataframe, target_value='332'):
    # Create a DataFrame with Boolean values indicating the presence of the target value
    presence_df = dataframe.eq(target_value)
    
    # Create a heatmap to visualize the occurrences of the target value
    heatmap = sns.heatmap(presence_df, cmap='Greens', cbar=False)
    
    # Set the title of the heatmap
    heatmap.set_title(f'Occurrences of {target_value}')
    
    # Return the DataFrame and the Axes object of the heatmap
    return presence_df, heatmap