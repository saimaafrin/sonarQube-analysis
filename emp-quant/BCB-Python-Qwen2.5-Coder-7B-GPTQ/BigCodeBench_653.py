import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def task_func(dataframe, target_value='332'):
    # Create a DataFrame with Boolean values indicating the presence of the target value
    bool_df = dataframe.applymap(lambda x: x == target_value)
    
    # Create a heatmap using seaborn
    ax = sns.heatmap(bool_df, cmap='Greens', cbar=False)
    
    # Return the Boolean DataFrame and the Axes object
    return bool_df, ax