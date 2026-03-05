
import random
from collections import Counter

def task_func(values, weights, n_samples):
    """
    Sample random numbers based on a given weighted distribution and return a histogram of the samples.

    Args:
        values (list): A list of values to sample from.
        weights (list): A list of weights for each value in `values`.
        n_samples (int): The number of samples to generate.

    Returns:
        histogram (dict): A histogram as a dictionary with the values as keys and counts as values.
    """
    histogram = Counter()
    for _ in range(n_samples):
        sample = random.choices(values, weights=weights, k=1)[0]
        histogram[sample] += 1
    return histogram