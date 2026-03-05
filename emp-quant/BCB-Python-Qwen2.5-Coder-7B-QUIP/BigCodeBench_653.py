
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def task_func(dataframe, target_value='332'):
    # Create a DataFrame with Boolean values indicating the presence of the target value
    bool_df = (dataframe == target_value).astype(int)
    
    # Create a heatmap using seaborn
    heatmap = sns.heatmap(bool_df, annot=True, cmap='viridis')
    
    # Return the Boolean DataFrame and the Axes object
    return bool_df, heatmap