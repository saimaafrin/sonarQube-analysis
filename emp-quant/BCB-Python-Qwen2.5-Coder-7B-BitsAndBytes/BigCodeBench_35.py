
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df, target_values=[1, 3, 4]):
    """
    Replace all elements in DataFrame columns that do not exist in the target_values array with zeros,
    and then output the distribution of each column after replacing.

    Parameters:
    df (pd.DataFrame): Input DataFrame.
    target_values (list): List of values to keep in the DataFrame.

    Returns:
    list: A list of matplotlib.axes.Axes objects corresponding to each column's plot.
    """
    # Create a copy of the DataFrame to avoid modifying the original
    modified_df = df.copy()
    
    # Iterate over each column in the DataFrame
    for col in df.columns:
        # Replace values not in target_values with zero
        modified_df[col] = modified_df[col].apply(lambda x: x if x in target_values else 0)
    
    # Plot the distribution of each column after replacement
    plots = []
    for col in modified_df.columns:
        ax = sns.histplot(modified_df[col], kde=True, label=col)
        ax.set_title(f'Distribution of {col}')
        ax.legend()
        plots.append(ax)
    
    return plots