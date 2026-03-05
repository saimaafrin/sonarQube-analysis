
import random
from collections import Counter

def task_func(values, weights, n_samples):
    # Create a dictionary to store the samples
    histogram = Counter()

    # Generate the samples
    for i in range(n_samples):
        histogram[random.choices(values, weights)[0]] += 1

    return histogram