
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(s1, s2):
    # Create a DataFrame to hold the data for the swarm plot
    df = pd.DataFrame({'s1': s1, 's2': s2})
    
    # Create the swarm plot
    ax = sns.swarmplot(x='s1', y='s2', data=df, s=100, palette="deep")
    
    # Find the intersection points
    intersection_points = df[(df['s1'] == df['s2'])].drop_duplicates()
    
    # Draw red dashed lines at the intersecting data points
    for index, row in intersection_points.iterrows():
        ax.axvline(x=row['s1'], color='r', linestyle='--')
        ax.axhline(y=row['s2'], color='r', linestyle='--')
    
    # Get the number of unique intersecting data points
    intersection_count = len(intersection_points)
    
    # Return the Axes object and the count of intersection points
    return ax, intersection_count