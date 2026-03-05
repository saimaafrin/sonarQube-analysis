
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt

def task_func(a, b):
    # Calculate Euclidean distance between two lists
    dist = distance.euclidean(a, b)

    # Create a Pandas DataFrame with indices 'A' and 'B'
    df = pd.DataFrame({'A': a, 'B': b})

    # Draw the values with a line displaying the Euclidean distance
    fig, ax = plt.subplots()
    ax.plot(df['A'], df['B'], 'o-')
    ax.set_xlabel('A')
    ax.set_ylabel('B')
    ax.set_title('Euclidean Distance = {:.2f}'.format(dist))
    plt.show()

    return dist, df, ax