
import collections
import itertools
import matplotlib.pyplot as plt

# Constants
ITEMS = ['apple', 'banana']

def task_func(a, b, items=ITEMS):
    # Combine the two lists
    combined_list = a + b
    
    # Count the frequency of each item in the combined list
    item_counts = collections.Counter(combined_list)
    
    # Filter the counts to only include the predefined items
    filtered_counts = {item: item_counts[item] for item in items if item in item_counts}
    
    # Create a bar chart of the filtered counts
    fig, ax = plt.subplots()
    ax.bar(filtered_counts.keys(), filtered_counts.values())
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Predefined Items in Combined List')
    
    return ax