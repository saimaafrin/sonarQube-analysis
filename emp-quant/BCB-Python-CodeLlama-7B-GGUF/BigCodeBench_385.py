
import matplotlib.pyplot as plt
from collections import Counter
FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']
def task_func(fruit_dict):
    fruit_counts = Counter()
    for name, fruit in fruit_dict.items():
        if fruit in FRUITS:
            fruit_counts[fruit] += 1
    return fruit_counts, plt.bar(fruit_counts.keys(), fruit_counts.values())