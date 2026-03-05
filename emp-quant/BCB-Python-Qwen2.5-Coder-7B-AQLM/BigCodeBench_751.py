
import random
from collections import Counter

def task_func(values, weights, n_samples):
    # Ensure the weights sum to 1
    weights = [w / sum(weights) for w in weights]
    
    # Generate samples based on the weighted distribution
    samples = random.choices(values, weights, k=n_samples)
    
    # Create a histogram of the samples
    histogram = Counter(samples)
    
    return histogram