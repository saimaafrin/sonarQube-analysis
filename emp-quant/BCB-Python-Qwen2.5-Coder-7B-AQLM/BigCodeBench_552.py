
import collections
import itertools
import matplotlib.pyplot as plt

# Constants
ITEMS = ['apple', 'banana']

def task_func(a, b, items=ITEMS):
    # Combine the two lists
    combined_list = a + b
    
    # Count the frequency of each item in the combined list
    frequency_counter = collections.Counter(combined_list)
    
    # Filter the frequency counter to only include the predefined items
    filtered_frequency = {item: frequency_counter[item] for item in items if item in frequency_counter}
    
    # Prepare data for plotting
    items_to_plot = list(filtered_frequency.keys())
    frequencies_to_plot = list(filtered_frequency.values())
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(items_to_plot, frequencies_to_plot, color='blue')
    
    # Set labels and title
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    ax.set_title('Frequency of Predefined Items in Combined List')
    
    # Show the plot
    plt.show()
    
    return ax