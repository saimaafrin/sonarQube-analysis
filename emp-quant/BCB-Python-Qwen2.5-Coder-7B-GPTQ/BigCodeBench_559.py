import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
def task_func(a, b):
    # Calculate the Euclidean distance between the two lists
    euclidean_distance = distance.euclidean(a, b)
    
    # Create a Pandas DataFrame from the lists with indices 'A' and 'B'
    df = pd.DataFrame({'A': a, 'B': b}, index=['A', 'B'])
    
    # Draw the values with a line displaying the Euclidean distance
    ax = df.plot(kind='line', marker='o')
    ax.set_title(f'Euclidean Distance: {euclidean_distance:.2f}')
    ax.set_xlabel('Index')
    ax.set_ylabel('Values')
    
    return euclidean_distance, df, ax