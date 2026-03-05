
import random
from collections import Counter

def task_func(values, weights, n_samples):
    # Sample random numbers based on the given weighted distribution
    samples = random.choices(values, weights, k=n_samples)
    
    # Create a histogram of the samples
    histogram = Counter(samples)
    
    return histogram