import matplotlib.pyplot as plt
from collections import Counter
FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']
def task_func(fruit_dict):
    """
    Given a constant list of fruits in FRUITS, and a dictionary 'fruit_dict' with keys as people's names and values as their favorite fruit names, record the frequency of each fruits' occurence. Return a bar chart of the number of fruits for each fruit type and return the dictionary with fruit names as keys and their counts as values.
    """
    # Create a counter object to count the frequency of each fruit
    fruit_counter = Counter()
    for fruit in FRUITS:
        fruit_counter[fruit] = 0

    # Count the frequency of each fruit in the fruit_dict
    for name, fruit in fruit_dict.items():
        if fruit in fruit_counter:
            fruit_counter[fruit] += 1

    # Create a bar chart of the frequency of each fruit
    fig, ax = plt.subplots()
    ax.bar(FRUITS, fruit_counter.values())
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Frequency')
    ax.set_title('Fruit Frequency')

    # Return the dictionary with fruit names as keys and their counts as values
    return fruit_counter
fruit_dict = {'Alice': 'Apple', 'Bob': 'Banana', 'Charlie': 'Cherry', 'David': 'Date', 'Eve': 'Elderberry', 'Frank': 'Fig', 'Grace': 'Grape', 'Henry': 'Honeydew', 'Iris': 'Indian Prune', 'Jack': 'Jackfruit'}