
import seaborn as sns
import matplotlib.pyplot as plt
import random

def task_func(list_of_lists, seed=0):
    # Fill empty sublists with random integers
    for sublist in list_of_lists:
        if not sublist:
            sublist.extend(random.sample(range(101), 5))

    # Combine data from all sublists
    data = [item for sublist in list_of_lists for item in sublist]

    # Create histogram
    ax = sns.histplot(data, bins=50)

    # Customize plot
    ax.set_xlabel('Value')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of List of Lists')

    return ax