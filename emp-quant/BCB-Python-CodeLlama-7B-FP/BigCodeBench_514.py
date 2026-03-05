import pandas as pd
import matplotlib.pyplot as plt
def task_func(array):
    """
    Create a Pandas DataFrame from a 2D list and plot the sum of each column.
    """
    # Create a Pandas DataFrame from the 2D list
    df = pd.DataFrame(array, columns=['A', 'B', 'C', 'D', 'E'])

    # Calculate the sum of each column
    sums = df.sum(axis=0)

    # Create a matplotlib Axes object to plot the sums
    ax = plt.gca()

    # Plot the sums
    ax.plot(sums)

    # Set the title and labels
    ax.set_title('Sum of each column')
    ax.set_xlabel('Column')
    ax.set_ylabel('Sum')

    # Return the DataFrame and Axes object
    return df, ax
array = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25]
]