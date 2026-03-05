import seaborn as sns
import matplotlib.pyplot as plt
import random
def task_func(list_of_lists, seed=0):
    """
    Create a histogram from the data in a list of lists. If any sublist is empty, it will be filled with 5 random integers ranging from 0 to 100 (both inclusive) The histogram will then be constructed using the combined data from all sublists.
    The function should output with:
        matplotlib.axes._axes.Axes: The histogram plot object.
    """
    # Check if the input is a list of lists
    if not isinstance(list_of_lists, list):
        raise ValueError("Input must be a list of lists")

    # Check if all sublists are lists
    for sublist in list_of_lists:
        if not isinstance(sublist, list):
            raise ValueError("All sublists must be lists")

    # Check if all sublists are non-empty
    for sublist in list_of_lists:
        if len(sublist) == 0:
            raise ValueError("All sublists must be non-empty")

    # Fill empty sublists with random integers
    for sublist in list_of_lists:
        if len(sublist) == 0:
            sublist.extend(random.sample(range(101), 5))

    # Combine data from all sublists
    data = []
    for sublist in list_of_lists:
        data.extend(sublist)

    # Create histogram
    ax = sns.histplot(data, kde=True, stat="density")

    # Set x-axis label
    ax.set_xlabel("Value")

    # Set y-axis label
    ax.set_ylabel("Frequency")

    # Set title
    ax.set_title("Histogram of Data")

    return ax
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]