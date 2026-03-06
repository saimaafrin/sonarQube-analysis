
import collections
import itertools
import matplotlib.pyplot as plt

# Constants
ITEMS = ['apple', 'banana']

def task_func(a, b, items=ITEMS):
    # Combine the two lists
    combined_list = list(itertools.chain(a, b))
    
    # Count the frequency of each item in the combined list
    counter = collections.Counter(combined_list)
    
    # Filter the counter to only include the predefined items
    filtered_counter = {item: counter[item] for item in items if item in counter}
    
    # Extract items and their frequencies
    items_list = list(filtered_counter.keys())
    frequencies = list(filtered_counter.values())
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(items_list, frequencies, color='blue')
    
    # Set labels and title
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Predefined Items in Combined List')
    
    return ax

ax = task_func(a, b)
plt.show()