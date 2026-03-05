import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(s1, s2):
    """
    Visualize two Series using a swarm plot with a highlight on their intersecting data points.
    
    Parameters:
    s1 (pd.Series): The first pandas Series.
    s2 (pd.Series): The second pandas Series.
    
    Returns:
    ax (matplotlib.Axes): The Axes object of the plotted swarm chart.
    intersection_count (int): The number of unique intersecting data points between s1 and s2.
    """
    # Create a DataFrame to hold the data
    df = pd.DataFrame({'s1': s1, 's2': s2})
    
    # Create a swarm plot
    ax = sns.swarmplot(data=df)
    
    # Find the intersection points
    intersection_points = df[(df['s1'] == df['s2'])]
    intersection_count = len(intersection_points)
    
    # Highlight the intersection points with red dashed lines
    for _, row in intersection_points.iterrows():
        ax.axhline(y=row['s1'], color='red', linestyle='--')
    
    return ax, intersection_count
s1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
s2 = pd.Series([2, 4, 6, 8, 10, 12, 14, 16, 18, 20])