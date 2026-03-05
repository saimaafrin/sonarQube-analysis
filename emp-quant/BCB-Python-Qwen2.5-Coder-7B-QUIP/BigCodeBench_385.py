
import matplotlib.pyplot as plt
from collections import Counter

FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']

def task_func(fruit_dict):
    # Initialize a Counter to keep track of fruit counts
    fruit_counter = Counter()

    # Iterate over the values in the fruit_dict and update the counter
    for fruit in fruit_dict.values():
        fruit_counter[fruit] += 1

    # Create a bar chart of the fruit counts
    fig, ax = plt.subplots()
    ax.bar(fruit_counter.keys(), fruit_counter.values())
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Count')
    ax.set_title('Fruit Frequency')

    # Return the dictionary with fruit counts and the axes object
    return fruit_counter, ax