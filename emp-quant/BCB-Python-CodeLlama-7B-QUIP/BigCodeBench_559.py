
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt

def task_func(a, b):
    # Calculate the Euclidean distance between the two lists
    dist = distance.euclidean(a, b)
    # Create a DataFrame with indices 'A' and 'B'
    df = pd.DataFrame({'A': a, 'B': b})
    # Plot the values with a line
    ax = plt.figure().add_subplot(111)
    ax.plot(a, b, 'o-')
    ax.set_xlabel('A')
    ax.set_ylabel('B')
    ax.set_title('Euclidean distance: {}'.format(dist))
    return dist, df, ax