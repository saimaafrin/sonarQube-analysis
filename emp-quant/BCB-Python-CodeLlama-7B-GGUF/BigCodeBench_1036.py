
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(s1, s2):
    # Create a swarm plot of the two series
    ax = sns.swarmplot(x=s1, y=s2)

    # Get the intersection points between the two series
    intersection_points = s1[s1.isin(s2)].index

    # Draw red dashed lines at the intersection points
    for point in intersection_points:
        ax.plot(point, point, 'r--')

    # Get the number of unique intersecting data points
    intersection_count = len(intersection_points)

    return ax, intersection_count

# Plot the swarm plot
plt.show()

# Print the number of intersecting data points
print(f"Number of intersecting data points: {intersection_count}")