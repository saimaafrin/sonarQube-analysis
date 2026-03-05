
import matplotlib.pyplot as plt
from collections import Counter
FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']
def task_func(fruit_dict):
    # Count the frequency of each fruit
    fruit_counter = Counter(fruit for person, fruit in fruit_dict.items())
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(fruit_counter.keys(), fruit_counter.values())
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Count')
    ax.set_title('Fruit Frequency')
    
    # Return the dictionary and the axes object
    return fruit_counter, ax