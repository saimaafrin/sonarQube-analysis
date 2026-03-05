
import matplotlib.pyplot as plt
from collections import Counter
FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']

def task_func(fruit_dict):
    # Initialize a counter to keep track of fruit frequencies
    fruit_counter = Counter()
    
    # Iterate through each person's favorite fruit and update the counter
    for fruit in fruit_dict.values():
        fruit_counter[fruit] += 1
    
    # Create a bar chart of the fruit frequencies
    fig, ax = plt.subplots()
    ax.bar(fruit_counter.keys(), fruit_counter.values())
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Frequency')
    ax.set_title('Fruit Frequency Chart')
    
    # Return the dictionary with fruit counts and the axes object of the plot
    return fruit_counter, ax