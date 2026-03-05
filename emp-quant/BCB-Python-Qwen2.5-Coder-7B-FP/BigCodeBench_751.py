import random
from collections import Counter
def task_func(values, weights, n_samples):
    """
    Sample random numbers based on a given weighted distribution and return a histogram of the samples.
    
    Parameters:
    values (list): A list of values to sample from.
    weights (list): A list of weights corresponding to the values.
    n_samples (int): The number of samples to draw.
    
    Returns:
    histogram (dict): A histogram as a dictionary with the values as keys and counts as values.
    """
    # Ensure the weights sum up to 1 for proper sampling
    weights = [w / sum(weights) for w in weights]
    
    # Sample the values based on the weights
    samples = random.choices(values, weights=weights, k=n_samples)
    
    # Create a histogram of the samples
    histogram = dict(Counter(samples))
    
    return histogram
values = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.2, 0.2]
n_samples = 1000