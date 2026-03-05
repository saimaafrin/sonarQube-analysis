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
    frequency_dict = collections.Counter(combined_list)
    # Filter the dictionary to only include the predefined items
    filtered_dict = {item: frequency_dict[item] for item in items}
    # Create a bar chart showing the frequency of the predefined items
    ax = plt.axes()
    ax.bar(filtered_dict.keys(), filtered_dict.values())
    ax.set_xlabel('Item')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Predefined Items')
    return ax
a = ['apple', 'banana']
b = ['banana', 'orange']