
import matplotlib.pyplot as plt
from collections import Counter
FRUITS = ['Apple', 'Banana', 'Cherry', 'Date', 'Elderberry', 'Fig', 'Grape', 'Honeydew', 'Indian Prune', 'Jackfruit']
def task_func(fruit_dict):
    fruit_counts = Counter()
    for fruit in FRUITS:
        fruit_counts[fruit] = 0
    for name, fruit in fruit_dict.items():
        fruit_counts[fruit] += 1
    fruit_counts = sorted(fruit_counts.items(), key=lambda x: x[1], reverse=True)
    fig, ax = plt.subplots()
    ax.bar(fruit_counts[:, 0], fruit_counts[:, 1])
    ax.set_xlabel('Fruit')
    ax.set_ylabel('Count')
    ax.set_title('Fruit Frequency')
    ax.set_xticks(range(len(fruit_counts)))
    ax.set_xticklabels(fruit_counts[:, 0])
    ax.set_yticks(range(len(fruit_counts)))
    ax.set_yticklabels(fruit_counts[:, 1])
    return dict(fruit_counts), ax