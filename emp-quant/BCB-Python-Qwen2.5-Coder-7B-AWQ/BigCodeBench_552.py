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
    filtered_counter = {item: frequency_counter[item] for item in items if item in frequency_counter}
    
    # Prepare data for plotting
    labels = list(filtered_counter.keys())
    values = list(filtered_counter.values())
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(labels, values, color='blue')
    
    # Set the title and labels
    ax.set_title('Frequency of Predefined Items in Combined List')
    ax.set_xlabel('Items')
    ax.set_ylabel('Frequency')
    
    return ax