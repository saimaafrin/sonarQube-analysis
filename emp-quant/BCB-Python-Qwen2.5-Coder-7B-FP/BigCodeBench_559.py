import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
def task_func(a, b):
    # Calculate the Euclidean distance between the two lists
    euclidean_distance = distance.euclidean(a, b)
    
    # Create a Pandas DataFrame from the lists with indices 'A' and 'B'
    df = pd.DataFrame({'A': a, 'B': b}, index=[0])
    
    # Draw the values with a line displaying the Euclidean distance
    fig, ax = plt.subplots()
    ax.plot(df['A'], label='A')
    ax.plot(df['B'], label='B')
    ax.legend()
    ax.set_title(f'Euclidean Distance: {euclidean_distance:.2f}')
    
    return euclidean_distance, df, ax