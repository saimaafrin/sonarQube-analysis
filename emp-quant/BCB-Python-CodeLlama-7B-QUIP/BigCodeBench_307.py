
import seaborn as sns
import matplotlib.pyplot as plt
import random

def task_func(list_of_lists, seed=0):
    # Check if any sublist is empty
    for sublist in list_of_lists:
        if not sublist:
            # Fill the empty sublist with 5 random integers
            sublist.extend(random.sample(range(0, 101), 5))

    # Combine the data from all sublists
    data = [item for sublist in list_of_lists for item in sublist]

    # Create the histogram plot
    fig, ax = plt.subplots()
    ax.hist(data, bins=50)
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Lists")
    return ax