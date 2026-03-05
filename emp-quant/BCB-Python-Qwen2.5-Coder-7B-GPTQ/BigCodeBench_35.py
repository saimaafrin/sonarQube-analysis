import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
def task_func(df, target_values=[1, 3, 4]):
    """
    Replace all elements in DataFrame columns that do not exist in the target_values array with zeros,
    and then output the distribution of each column after replacing.
    - label each plot as the name of the column it corresponds to.
    
    Parameters:
    - df: pandas DataFrame to process.
    - target_values: List of values to keep in the DataFrame. Defaults to [1, 3, 4].
    
    Returns:
    - matplotlib.axes.Axes: The Axes object of the plotted data.
    """
    # Replace values not in target_values with 0
    for column in df.columns:
        df[column] = df[column].apply(lambda x: x if x in target_values else 0)
    
    # Plot the distribution of each column
    fig, axes = plt.subplots(nrows=len(df.columns), ncols=1, figsize=(8, 2*len(df.columns)))
    for i, column in enumerate(df.columns):
        sns.histplot(df[column], ax=axes[i], kde=True)
        axes[i].set_title(f'Distribution of {column}')
    
    plt.tight_layout()
    plt.show()
    return axes