import random
from collections import Counter
def task_func(values, weights, n_samples):
    """
    Sample random numbers based on a given weighted distribution and return a histogram of the samples.
    
    :param values: A list of values to sample from.
    :param weights: A list of weights corresponding to the values.
    :param n_samples: The number of samples to draw.
    :return: A histogram as a dictionary with the values as keys and counts as values.
    """
    # Ensure the values and weights lists are of the same length
    if len(values) != len(weights):
        raise ValueError("Values and weights must be of the same length.")
    
    # Normalize the weights
    total_weight = sum(weights)
    normalized_weights = [w / total_weight for w in weights]
    
    # Sample the values based on the normalized weights
    samples = random.choices(values, weights=normalized_weights, k=n_samples)
    
    # Create a histogram of the samples
    histogram = Counter(samples)
    
    return histogram
values = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.2, 0.2]
n_samples = 1000