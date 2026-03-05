import pandas as pd
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
    df_bool = dataframe.eq(target_value, axis=0)

    # Create a heatmap of the Boolean values
    ax = sns.heatmap(df_bool, annot=True, cmap='RdYlGn')

    # Return the DataFrame and Axes object
    return df_bool, ax
dataframe = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10]})
target_value = 3