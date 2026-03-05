
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def task_func(dataframe, target_value='332'):
    """
    Searches a given DataFrame for occurrences of a specified target value and visualizes these occurrences using a heatmap.
    
    Parameters:
    - dataframe: pd.DataFrame, the input DataFrame to search.
    - target_value: str, the value to search for in the DataFrame. Default is '332'.
    
    Returns:
    - tuple: A tuple containing:
        - pd.DataFrame: A DataFrame with Boolean values indicating the presence of the target value in the input DataFrame.
        - matplotlib.axes._axes.Axes: The Axes object of the heatmap.
    """
    # Create a DataFrame with Boolean values indicating the presence of the target value
    target_df = dataframe == target_value
    
    # Create a heatmap using seaborn
    plt.figure(figsize=(10, 6))
    heatmap = sns.heatmap(target_df, cmap='Greens', cbar=False)
    
    # Return the target DataFrame and the heatmap Axes object
    return target_df, heatmap