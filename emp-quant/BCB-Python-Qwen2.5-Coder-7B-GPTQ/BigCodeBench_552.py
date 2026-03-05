import collections
import itertools
import matplotlib.pyplot as plt
ITEMS = ['apple', 'banana']
def task_func(a, b, items=ITEMS):
    # Combine the two lists
    combined_list = a + b
    
    # Count the frequency of each item in the combined list
    frequency_counter = collections.Counter(combined_list)
    
    # Filter the frequency counter to only include the predefined items
    filtered_frequency = {item: frequency_counter.get(item, 0) for item in items}
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(filtered_frequency.keys(), filtered_frequency.values())
    
    # Set the title and labels
    ax.set_title('Frequency of Predefined Items in Combined List')
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    
    return ax