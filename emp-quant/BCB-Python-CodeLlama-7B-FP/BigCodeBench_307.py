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

    # Set x-axis label
    ax.set_xlabel("Value")

    # Set y-axis label
    ax.set_ylabel("Frequency")

    # Set title
    ax.set_title("Histogram of Data")

    # Return histogram plot object
    return ax
list_of_lists = [
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [100, 200, 300, 400, 500],
    [],
    [],
    [],
]
data = [item for sublist in list_of_lists for item in sublist]
ax = sns.histplot(data, bins=50)