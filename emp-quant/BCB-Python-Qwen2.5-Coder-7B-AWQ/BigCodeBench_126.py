import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np
def task_func(animals=None, seed=42):
    random_seed(seed)
    if animals is None:
        animals = ['Lion', 'Tiger', 'Bear', 'Elephant', 'Giraffe']
    
    data = []
    for animal in animals:
        counts = [randint(1, 100) for _ in range(10)]
        mean = np.mean(counts)
        median = np.median(counts)
        std_dev = np.std(counts)
        data.append([animal, mean, median, std_dev])
    
    df = pd.DataFrame(data, columns=['Animal', 'Mean', 'Median', 'Standard Deviation'])
    return df