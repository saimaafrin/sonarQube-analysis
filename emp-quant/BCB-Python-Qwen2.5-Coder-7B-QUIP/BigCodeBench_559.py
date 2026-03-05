
import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt

def task_func(a, b):
    # Calculate the Euclidean distance between the two lists
    euclidean_distance = distance.euclidean(a, b)
    
    # Create a DataFrame from the lists with indices 'A' and 'B'
    df = pd.DataFrame({'A': a, 'B': b})
    
    # Plot the values with a line displaying the Euclidean distance
    fig, ax = plt.subplots()
    ax.plot(a, label='A')
    ax.plot(b, label='B')
    ax.set_title(f'Euclidean Distance: {euclidean_distance}')
    ax.legend()
    
    return euclidean_distance, df, ax