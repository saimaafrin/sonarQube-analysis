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

    # Get the intersection points between the two Series
    intersection_points = s1[s1.isin(s2)].index

    # Draw red dashed lines at the intersection points
    for point in intersection_points:
        ax.axvline(x=point, color='red', linestyle='dashed')

    # Return the Axes object and the number of intersection points
    return ax, len(intersection_points)
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([2, 3, 4, 5, 6])