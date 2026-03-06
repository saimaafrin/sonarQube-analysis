import pandas as pd
import matplotlib.pyplot as plt
def task_func(data, column):
    """
    Draw and return a bar chart that shows the distribution of categories in a specific column of a dictionary.
    
    Note:
    The categories are defined by the constant CATEGORIES, 
    which is a list containing ['A', 'B', 'C', 'D', 'E']. If some categories are missing in the DataFrame, 
    they will be included in the plot with a count of zero.
    The x label of the plot is set to 'Category', the y label is set to 'Count', and the title is set to 'Distribution of {column}'.
    
    Parameters:
    - data (dict): A dictionary where the keys are the column names and the values are the column values.
    - column (str): The name of the column in the DataFrame that contains the categories.
    
    Returns:
    - matplotlib.axes._axes.Axes: The Axes object for the generated plot.
    
    Requirements:
    - pandas
    - numpy
    - matplotlib.pyplot
    
    Example:
    >>> data = {'Category': ['A', 'B', 'B', 'C', 'A', 'D', 'E', 'E', 'D']}
    >>> ax = task_func(data, 'Category')    
    >>> data = {'Type': ['A', 'A', 'C', 'E', 'D', 'E', 'D']}
    >>> ax = task_func(data, 'Type')
    """
    # Create a DataFrame from the dictionary
    df = pd.DataFrame(data)
    # Create a list of all categories
    categories = ['A', 'B', 'C', 'D', 'E']
    # Create a list of all categories in the DataFrame
    df_categories = df[column].unique().tolist()
    # Create a list of all categories that are not in the DataFrame
    missing_categories = [category for category in categories if category not in df_categories]
    # Create a list of all categories that are in the DataFrame
    df_categories = [category for category in df_categories if category in categories]
    # Create a list of all categories that are in the DataFrame and their counts
    df_categories_counts = [(category, df[df[column] == category][column].count()) for category in df_categories]
    # Create a list of all categories that are not in the DataFrame and their counts
    missing_categories_counts = [(category, 0) for category in missing_categories]
    # Create a list of all categories and their counts
    categories_counts = df_categories_counts + missing_categories_counts
    # Create a DataFrame from the list of categories and their counts
    df_categories_counts = pd.DataFrame(categories_counts, columns=['Category', 'Count'])
    # Create a bar chart
    ax = df_categories_counts.plot.bar(x='Category', y='Count', title=f'Distribution of {column}')
    # Return the Axes object
    return ax