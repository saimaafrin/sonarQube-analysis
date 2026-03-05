import collections
import itertools
import matplotlib.pyplot as plt
ITEMS = ['apple', 'banana']
def task_func(a, b, items=ITEMS):
    """Combine two lists and record the frequency of predefined items in the combined list.

    Args:
        a (list): First list.
        b (list): Second list.
        items (list, optional): Predefined items. Defaults to ITEMS.

    Returns:
        matplotlib.axes.Axes: A bar chart showing the frequency of predefined items in the combined list.
    """
    # Combine the two lists
    combined_list = a + b

    # Record the frequency of predefined items in the combined list
    frequency_dict = collections.Counter(combined_list)

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(items, frequency_dict.values())
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Predefined Items in the Combined List')

    return ax
a = ['apple', 'banana']
b = ['banana', 'orange']