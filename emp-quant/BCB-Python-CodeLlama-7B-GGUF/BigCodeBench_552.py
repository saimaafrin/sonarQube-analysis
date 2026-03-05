
import collections
import itertools
import matplotlib.pyplot as plt

# Constants
ITEMS = ['apple', 'banana']

def task_func(a, b, items=ITEMS):
    # Combine the two lists
    combined_list = list(itertools.chain(a, b))

    # Count the frequency of each item in the combined list
    item_counts = collections.Counter(combined_list)

    # Create a bar chart showing the frequency of each item
    fig, ax = plt.subplots()
    ax.bar(range(len(ITEMS)), [item_counts[item] for item in ITEMS])
    ax.set_xticks(range(len(ITEMS)))
    ax.set_xticklabels(ITEMS)
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Predefined Items')

    return ax