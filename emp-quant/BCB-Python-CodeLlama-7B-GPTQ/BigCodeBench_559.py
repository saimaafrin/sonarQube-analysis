import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
def task_func(a, b):
    """
    Calculate the Euclidean distance between two lists, create a Pandas DataFrame from these lists with indices 'A' and 'B', and then draw the values with a line displaying the Euclidean distance.
    The function should output with:
        float: The computed Euclidean distance between the two lists.
        pd.DataFrame: A DataFrame containing the two lists as columns.
        matplotlib.axes.Axes: The generated plot's Axes object.
    """
    # Calculate the Euclidean distance between the two lists
    dist = distance.euclidean(a, b)

    # Create a Pandas DataFrame with the two lists as columns
    df = pd.DataFrame({'A': a, 'B': b})

    # Draw the values with a line displaying the Euclidean distance
    fig, ax = plt.subplots()
    ax.plot(df['A'], df['B'], 'o-')
    ax.set_xlabel('List A')
    ax.set_ylabel('List B')
    ax.set_title('Euclidean Distance')
    ax.axvline(x=dist, color='red', linestyle='--')
    ax.text(dist, 0, f'Euclidean Distance: {dist:.2f}', ha='center')

    return dist, df, ax
a = [1, 2, 3, 4, 5]
b = [2, 4, 6, 8, 10]