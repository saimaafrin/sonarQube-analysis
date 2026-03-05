import collections
import itertools
import matplotlib.pyplot as plt
ITEMS = ['apple', 'banana']
def task_func(a, b, items=ITEMS):
    # Combine the two lists
    combined_list = a + b
    
    # Count the frequency of each item in the combined list
    frequency_counter = collections.Counter(combined_list)
    
    # Filter the frequency counter to include only the predefined items
    filtered_frequency = {item: frequency_counter.get(item, 0) for item in items}
    
    # Prepare data for plotting
    items_to_plot = list(filtered_frequency.keys())
    frequencies_to_plot = list(filtered_frequency.values())
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(items_to_plot, frequencies_to_plot)
    
    # Set labels and title
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Predefined Items in Combined List')
    
    return ax