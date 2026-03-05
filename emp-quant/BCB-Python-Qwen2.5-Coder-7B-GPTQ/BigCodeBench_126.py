import pandas as pd
from random import randint, seed as random_seed
import statistics
import numpy as np
def task_func(animals=None, seed=42):
    if animals is None:
        animals = ['Lion', 'Elephant', 'Giraffe', 'Zebra', 'Kangaroo']
    
    random_seed(seed)
    data = []
    
    for animal in animals:
        counts = [randint(1, 100) for _ in range(10)]
        mean = statistics.mean(counts)
        median = statistics.median(counts)
        std_dev = statistics.stdev(counts)
        
        data.append([animal, mean, median, std_dev])
    
    df = pd.DataFrame(data, columns=['Animal', 'Mean', 'Median', 'Standard Deviation'])
    return df