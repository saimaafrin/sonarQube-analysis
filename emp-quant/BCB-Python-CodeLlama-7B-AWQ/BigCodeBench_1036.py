import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
def task_func(s1, s2):
    """
    Visualize two Series using a swarm plot with a highlight on their intersecting data points.
    This function creates a swarm plot to visually compare two pandas Series. It highlights the intersection points between these two series by drawing red dashed lines at the intersecting data points.
    The function should output with:
        ax (matplotlib.Axes): The Axes object of the plotted swarm chart. This object can be used for further customization of the plot if required.
        intersection_count (int): The number of unique intersecting data points between s1 and s2.
        This count gives a quick numerical summary of the overlap between the two series.
    """
    # Create a swarm plot of the two Series
    ax = sns.swarmplot(x=s1, y=s2)

    # Get the unique data points in both Series
    s1_unique = set(s1)
    s2_unique = set(s2)
    intersection = s1_unique.intersection(s2_unique)

    # Draw red dashed lines at the intersecting data points
    for point in intersection:
        ax.plot([point, point], [0, 1], 'r--')

    # Return the Axes object and the number of intersecting data points
    return ax, len(intersection)
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([2, 3, 4, 5, 6])