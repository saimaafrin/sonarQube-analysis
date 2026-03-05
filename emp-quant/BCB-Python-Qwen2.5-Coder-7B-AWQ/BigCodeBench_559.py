import pandas as pd
from scipy.spatial import distance
import matplotlib.pyplot as plt
def task_func(a, b):
    """
    Calculate the Euclidean distance between two lists, create a Pandas DataFrame from these lists with indices 'A' and 'B',
    and then draw the values with a line displaying the Euclidean distance.
    
    Parameters:
    a (list): The first list of numbers.
    b (list): The second list of numbers.
    
    Returns:
    float: The computed Euclidean distance between the two lists.
    pd.DataFrame: A DataFrame containing the two lists as columns.
    matplotlib.axes.Axes: The generated plot's Axes object.
    """
    # Calculate Euclidean distance
    euclidean_distance = distance.euclidean(a, b)
    
    # Create DataFrame
    df = pd.DataFrame({'A': a, 'B': b})
    
    # Plot the values
    fig, ax = plt.subplots()
    ax.plot(df['A'], label='A')
    ax.plot(df['B'], label='B')
    ax.axhline(y=euclidean_distance, color='r', linestyle='--', label=f'Euclidean Distance: {euclidean_distance}')
    ax.legend()
    
    return euclidean_distance, df, ax
a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]