
import matplotlib.pyplot as plt
from collections import Counter

FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']

def task_func(fruit_dict):
    # Create a Counter object to keep track of the frequency of each fruit
    fruit_counter = Counter()
    for fruit in FRUITS:
        fruit_counter[fruit] = 0

    # Iterate over the fruit_dict and increment the frequency of each fruit
    for name, fruit in fruit_dict.items():
        if fruit in fruit_counter:
            fruit_counter[fruit] += 1

    # Create a bar chart of the frequency of each fruit
    fig, ax = plt.subplots()
    ax.bar(FRUITS, fruit_counter.values())
    ax.set_title('Fruit Frequency')
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Frequency')
    ax.set_xticks(range(len(FRUITS)))
    ax.set_xticklabels(FRUITS)

    # Return the dictionary with fruit names as keys and their counts as values
    return {fruit: count for fruit, count in fruit_counter.items()}

# Call the function and print the resulting dictionary
result = task_func(fruit_dict)
print(result)

# Plot the bar chart
fig, ax = plt.subplots()
ax.bar(FRUITS, fruit_counter.values())
ax.set_title('Fruit Frequency')
ax.set_xlabel('Fruit')
ax.set_ylabel('Frequency')
ax.set_xticks(range(len(FRUITS)))
ax.set_xticklabels(FRUITS)
plt.show()