import pandas as pd
import matplotlib.pyplot as plt
def task_func(data, column):
    """
    Draw and return a bar chart that shows the distribution of categories in a specific column of a dictionary.
    """
    # Create a new DataFrame with the specified column
    df = pd.DataFrame(data, columns=[column])

    # Create a new DataFrame with the categories and their counts
    df_categories = pd.DataFrame(df[column].value_counts())
    df_categories.columns = ['Count']
    df_categories.index.name = 'Category'

    # Plot the distribution of categories
    ax = df_categories.plot(kind='bar', x='Category', y='Count', title=f'Distribution of {column}')

    # Set the x label and y label
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')

    # Return the Axes object for the generated plot
    return ax
data = {'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25]}
column = 'A'