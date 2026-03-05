import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def task_func(dataframe, target_value='332'):
    # Create a DataFrame with Boolean values indicating the presence of the target value
    presence_df = dataframe.applymap(lambda x: x == target_value)
    
    # Create a heatmap using seaborn
    heatmap = sns.heatmap(presence_df, cmap='coolwarm', cbar=False)
    
    # Return the Boolean DataFrame and the Axes object of the heatmap
    return presence_df, heatmap