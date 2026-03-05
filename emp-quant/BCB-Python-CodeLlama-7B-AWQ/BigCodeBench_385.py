import matplotlib.pyplot as plt
from collections import Counter
FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']
def task_func(fruit_dict):
    """
    Given a constant list of fruits in FRUITS, and a dictionary 'fruit_dict' with keys as people's names and values as their favorite fruit names, record the frequency of each fruits' occurence. Return a bar chart of the number of fruits for each fruit type and return the dictionary with fruit names as keys and their counts as values.
    """
    # Create a counter to keep track of the frequency of each fruit
    fruit_counter = Counter()

    # Iterate over the dictionary and increment the counter for each fruit
    for person, fruit in fruit_dict.items():
        if fruit in FRUITS:
            fruit_counter[fruit] += 1

    # Create a bar chart of the frequency of each fruit
    ax = plt.bar(FRUITS, fruit_counter.values())

    # Return the dictionary with fruit names as keys and their counts as values
    return {fruit: count for fruit, count in fruit_counter.items()}
fruit_dict = {'Alice': 'Apple', 'Bob': 'Banana', 'Charlie': 'Cherry', 'David': 'Date', 'Eve': 'Elderberry', 'Frank': 'Fig', 'Grace': 'Grape', 'Helen': 'Honeydew', 'Ivan': 'Indian Prune', 'Jack': 'Jackfruit'}