
import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np

def task_func(animals=None, seed=42):
    if animals is None:
        animals = ['Lion', 'Tiger', 'Bear', 'Elephant', 'Giraffe', 'Kangaroo', 'Panda', 'Monkey', 'Zebra', 'Rabbit']
    
    random_seed(seed)
    data = {}
    
    for animal in animals:
        counts = [randint(1, 100) for _ in range(10)]
        data[animal] = counts
    
    stats = []
    for animal, counts in data.items():
        mean = np.mean(counts)
        median = np.median(counts)
        std_dev = np.std(counts)
        stats.append([animal, mean, median, std_dev])
    
    df = pd.DataFrame(stats, columns=['Animal', 'Mean', 'Median', 'Standard Deviation'])
    
    return df

# Function to plot the bar chart
def plot_bar_chart(report):
    import matplotlib.pyplot as plt
    plt.figure(figsize=(10, 6))
    plt.bar(report['Animal'], report['Mean'], color='b', alpha=0.7)
    plt.xlabel('Animal')
    plt.ylabel('Mean Count')
    plt.title('Mean Animal Count in Zoo')
    plt.show()