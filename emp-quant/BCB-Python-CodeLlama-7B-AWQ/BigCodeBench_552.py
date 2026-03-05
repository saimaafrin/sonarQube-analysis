import collections
import itertools
import matplotlib.pyplot as plt
ITEMS = ['apple', 'banana']
def task_func(a, b, items=ITEMS):
    """
    Combine two lists and record the frequency of predefined items in the combined list.
    """
    # Combine the two lists
    combined_list = a + b
    # Create a dictionary to store the frequency of each item
    freq_dict = collections.defaultdict(int)
    # Iterate through the combined list and increment the frequency of each item
    for item in combined_list:
        freq_dict[item] += 1
    # Create a list of tuples containing the items and their frequencies
    freq_list = [(item, freq_dict[item]) for item in items]
    # Sort the list by frequency in descending order
    freq_list.sort(key=lambda x: x[1], reverse=True)
    # Create a bar chart showing the frequency of predefined items in the combined list
    fig, ax = plt.subplots()
    ax.bar(range(len(freq_list)), [x[1] for x in freq_list], label='Frequency')
    ax.set_xticks(range(len(freq_list)))
    ax.set_xticklabels([x[0] for x in freq_list])
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Predefined Items in Combined List')
    return ax
a = ['apple', 'banana']
b = ['apple', 'orange']