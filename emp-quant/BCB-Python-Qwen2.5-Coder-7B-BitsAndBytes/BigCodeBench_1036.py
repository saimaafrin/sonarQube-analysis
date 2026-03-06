
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(s1, s2):
    """
    Creates a swarm plot to visually compare two pandas Series and highlights their intersecting data points.
    
    Parameters:
    s1 (pd.Series): First pandas Series.
    s2 (pd.Series): Second pandas Series.
    
    Returns:
    ax (matplotlib.Axes): The Axes object of the plotted swarm chart.
    intersection_count (int): The number of unique intersecting data points between s1 and s2.
    """
    # Combine the Series into a DataFrame
    df = pd.DataFrame({'Series1': s1, 'Series2': s2})
    
    # Create a swarm plot
    ax = sns.swarmplot(data=df)
    
    # Find the intersection points
    intersection_points = set(s1).intersection(set(s2))
    intersection_count = len(intersection_points)
    
    # Highlight the intersection points with red dashed lines
    for point in intersection_points:
        ax.axvline(x=point, color='red', linestyle='--')
    
    return ax, intersection_count

    # Call the function
    ax, intersection_count = task_func(s1, s2)
    
    # Show the plot
    plt.show()
    
    # Print the intersection count
    print(f"Number of intersecting data points: {intersection_count}")