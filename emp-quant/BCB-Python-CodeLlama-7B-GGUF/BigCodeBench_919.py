
import pandas as pd
import matplotlib.pyplot as plt

CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(data, column):
    # Create a new DataFrame with the specified column
    df = pd.DataFrame(data[column])

    # Create a new DataFrame with the categories and counts
    categories = pd.DataFrame(CATEGORIES, columns=['Category'])
    categories['Count'] = 0

    # Merge the two DataFrames
    merged = pd.merge(categories, df, on='Category')

    # Sort the DataFrame by category
    merged.sort_values(by='Category', inplace=True)

    # Create the bar chart
    ax = merged.plot.bar(x='Category', y='Count', title=f'Distribution of {column}')

    # Set the x label
    ax.set_xlabel('Category')

    # Set the y label
    ax.set_ylabel('Count')

    # Return the Axes object
    return ax