
import random
from collections import Counter

def task_func(values, weights, n_samples):
    """
    Sample random numbers based on a given weighted distribution and return a histogram of the samples.
    
    Parameters:
    values (list): A list of possible values to sample from.
    weights (list): A list of weights corresponding to the values.
    n_samples (int): The number of samples to generate.
    
    Returns:
    histogram (dict): A histogram as a dictionary with the values as keys and counts as values.
    """
    # Ensure the length of values and weights are the same
    if len(values) != len(weights):
        raise ValueError("The length of values and weights must be the same.")
    
    # Normalize the weights
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    
    # Generate samples using the weighted distribution
    samples = random.choices(values, weights=normalized_weights, k=n_samples)
    
    # Create a histogram of the samples
    histogram = dict(Counter(samples))
    
    return histogram

histogram = task_func(values, weights, n_samples)
print(histogram)