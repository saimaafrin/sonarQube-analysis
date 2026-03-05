import random
from collections import Counter
def task_func(values, weights, n_samples):
    # Create a list of samples based on the weighted distribution
    samples = random.choices(values, weights, k=n_samples)
    
    # Count the occurrences of each value in the samples
    histogram = Counter(samples)
    
    return histogram