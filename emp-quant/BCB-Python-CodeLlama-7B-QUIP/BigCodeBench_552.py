
import collections
import itertools
import matplotlib.pyplot as plt
# Constants
ITEMS = ['apple', 'banana']
def task_func(a, b, items=ITEMS):
    # Combine the two lists
    combined_list = a + b
    # Create a counter for each item in the combined list
    counter = collections.Counter(combined_list)
    # Get the frequency of each item in the combined list
    freq = counter.most_common(len(items))
    # Create a bar chart showing the frequency of each item in the combined list
    plt.bar(freq)
    plt.show()
    return freq