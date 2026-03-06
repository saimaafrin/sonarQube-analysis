import collections
import itertools
import matplotlib.pyplot as plt
ITEMS = ['apple', 'banana']
def task_func(a, b, items=ITEMS):
    """
    Combine two lists and record the frequency of predefined items in the combined list.

    Parameters:
    a (list): A list of items.
    b (list): Another list of items.
    items (list, optional): a list of predefined items

    Returns:
    matplotlib.axes.Axes: A bar chart showing the frequency of predefined items in the combined list.

    Requirements:
    - collections
    - itertools
    - matplotlib.pyplot

    Example:
    >>> ax = task_func(['apple', 'banana', 'cherry'], ['date', 'elderberry', 'apple', 'banana', 'cherry'])
    >>> isinstance(ax, matplotlib.axes.Axes)
    True
    """
    # Combine two lists
    combined_list = a + b

    # Count the frequency of predefined items in the combined list
    counts = collections.Counter(combined_list)

    # Create a bar chart showing the frequency of predefined items in the combined list
    ax = plt.bar(range(len(items)), counts.values(), align='center')
    ax.set_xticks(range(len(items)))
    ax.set_xticklabels(items, rotation=45)
    ax.set_title('Frequency of predefined items in the combined list')
    ax.set_xlabel('Predefined items')
    ax.set_ylabel('Frequency')

    return ax