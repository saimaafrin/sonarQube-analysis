import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
def task_func(a, b):
    """
    Calculate the Euclidean distance between two lists, create a Pandas DataFrame from these lists with indices 'A' and 'B', and then draw the values with a line displaying the Euclidean distance.
    """
    # Calculate the Euclidean distance between the two lists
    dist = distance.euclidean(a, b)

    # Create a Pandas DataFrame with the two lists as columns
    df = pd.DataFrame({'A': a, 'B': b})

    # Draw the values with a line displaying the Euclidean distance
    fig, ax = plt.subplots()
    ax.plot(df['A'], df['B'], label='Euclidean distance = ' + str(dist))
    ax.set_xlabel('List A')
    ax.set_ylabel('List B')
    ax.set_title('Euclidean Distance between Lists')
    ax.legend()

    return dist, df, ax
a = [1, 2, 3]
b = [4, 5, 6]