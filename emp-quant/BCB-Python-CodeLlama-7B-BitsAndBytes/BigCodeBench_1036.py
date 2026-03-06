
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(s1, s2):
    # Create a swarm plot with the two series
    ax = sns.swarmplot(x=s1, y=s2)

    # Highlight the intersecting data points
    intersection_indices = s1[s1 == s2].index
    ax.plot(intersection_indices, s1.loc[intersection_indices], 'ro-', color='red')

    # Count the number of intersecting data points
    intersection_count = len(intersection_indices)

    return ax, intersection_count

# Plot the swarm plot with the highlighted intersecting data points
ax.set_title('Swarm Plot with Intersecting Data Points')
ax.set_xlabel('Series 1')
ax.set_ylabel('Series 2')
plt.show()

# Print the number of intersecting data points
print(f'Number of intersecting data points: {intersection_count}')