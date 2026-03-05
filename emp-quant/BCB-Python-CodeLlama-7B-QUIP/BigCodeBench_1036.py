
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(s1, s2):
    # Create a swarm plot of the two series
    ax = sns.swarmplot(s1, s2)

    # Highlight the intersecting data points
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            ax.axvlines(s1[i], s2[i], color='red', linestyle='dashed')

    # Return the Axes object and the number of intersecting data points
    return ax, len(set(s1).intersection(s2))