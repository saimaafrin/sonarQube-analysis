import seaborn as sns
import matplotlib.pyplot as plt
import random
def task_func(list_of_lists, seed=0):
    # Check if any sublist is empty
    if any(not sublist for sublist in list_of_lists):
        # Fill empty sublists with random integers
        for sublist in list_of_lists:
            if not sublist:
                sublist.extend(random.sample(range(101), 5))

    # Combine data from all sublists
    data = [item for sublist in list_of_lists for item in sublist]

    # Create histogram
    ax = sns.histplot(data, bins=50)

    # Set title and labels
    ax.set_title("Histogram of Data")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")

    return ax
list_of_lists = [
    [1, 2, 3, 4, 5],
    [10, 20, 30, 40, 50],
    [100, 200, 300, 400, 500],
    [],
    [],
    [],
]