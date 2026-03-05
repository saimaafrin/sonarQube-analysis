import pandas as pd
import matplotlib.pyplot as plt
def task_func(data, column):
    """
    Draw and return a bar chart that shows the distribution of categories in a specific column of a dictionary.
    """
    # Create a list of all categories
    categories = ['A', 'B', 'C', 'D', 'E']

    # Create a DataFrame with the data
    df = pd.DataFrame(data, columns=[column])

    # Create a new DataFrame with the data and the categories
    df_categories = pd.DataFrame(df[column].value_counts())
    df_categories = df_categories.reindex(categories)

    # Set the x label, y label, and title of the plot
    plt.xlabel('Category')
    plt.ylabel('Count')
    plt.title(f'Distribution of {column}')

    # Draw the bar chart
    ax = df_categories.plot.bar(rot=0)

    return ax
data = {'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15], 'D': [4, 8, 12, 16, 20], 'E': [5, 10, 15, 20, 25]}
column = 'A'