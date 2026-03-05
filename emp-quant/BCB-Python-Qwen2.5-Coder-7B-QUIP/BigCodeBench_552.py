
import collections
import itertools
import matplotlib.pyplot as plt
# Constants
ITEMS = ['apple', 'banana']
def task_func(a, b, items=ITEMS):
    # Combine the two lists
    combined = list(itertools.chain(a, b))
    
    # Count the frequency of each item in the combined list
    frequency = collections.Counter(combined)
    
    # Filter the frequency to only include the predefined items
    filtered_frequency = {item: frequency[item] for item in ITEMS if item in frequency}
    
    # Create a bar chart to visualize the frequency
    fig, ax = plt.subplots()
    ax.bar(filtered_frequency.keys(), filtered_frequency.values())
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Predefined Items')
    
    return ax