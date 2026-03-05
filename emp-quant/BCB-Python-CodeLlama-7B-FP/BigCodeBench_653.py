import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
def task_func(dataframe, target_value='332'):
    """
    Searches a given DataFrame for occurrences of a specified target value and visualizes these occurrences using a heatmap.
    The function should output with:
        tuple: A tuple containing:
            pd.DataFrame: A DataFrame with Boolean values indicating the presence of the target value in the input DataFrame.
            matplotlib.axes._axes.Axes: The Axes object of the heatmap.
    """
    # Create a DataFrame with Boolean values indicating the presence of the target value in the input DataFrame
    target_df = dataframe.isin([target_value])

    # Create a heatmap of the DataFrame
    ax = sns.heatmap(target_df, cmap='Blues')

    return target_df, ax
dataframe = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})
target_value = '3'