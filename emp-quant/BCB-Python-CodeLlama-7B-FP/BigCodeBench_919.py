import pandas as pd
import matplotlib.pyplot as plt
def task_func(data, column):
    """
    Draw and return a bar chart that shows the distribution of categories in a specific column of a dictionary.
    """
    # Create a list of all categories
    categories = ['A', 'B', 'C', 'D', 'E']

    # Create a dictionary to store the counts for each category
    counts = {}

    # Iterate over the data and increment the count for each category
    for row in data[column]:
        if row in counts:
            counts[row] += 1
        else:
            counts[row] = 1

    # Create a DataFrame to store the counts
    counts_df = pd.DataFrame(counts, index=categories)

    # Plot the counts
    ax = counts_df.plot(kind='bar', x='Category', y='Count', title=f'Distribution of {column}')

    # Set the x label and y label
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')

    # Return the Axes object for the generated plot
    return ax
data = {'A': [1, 2, 3, 4, 5], 'B': [2, 4, 6, 8, 10], 'C': [3, 6, 9, 12, 15], 'D': [4, 8, 12, 16, 20], 'E': [5, 10, 15, 20, 25]}
column = 'A'