
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt

def task_func(a, b):
    # Calculate the Euclidean distance between the two lists
    euclidean_distance = distance.euclidean(a, b)

    # Create a Pandas DataFrame with indices 'A' and 'B'
    df = pd.DataFrame({'A': a, 'B': b})

    # Draw the values with a line displaying the Euclidean distance
    fig, ax = plt.subplots()
    ax.plot(df['A'], df['B'], label='Euclidean distance = {:.2f}'.format(euclidean_distance))
    ax.set_xlabel('List A')
    ax.set_ylabel('List B')
    ax.set_title('Euclidean Distance between Lists')
    ax.legend()

    return euclidean_distance, df, ax