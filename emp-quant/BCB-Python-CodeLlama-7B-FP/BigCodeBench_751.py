import random
from collections import Counter
def task_func(values, weights, n_samples):
    """
    Sample random numbers based on a given weighted distribution and return a histogram of the samples.
    :param values: A list of values to sample from.
    :param weights: A list of weights for each value in values.
    :param n_samples: The number of samples to generate.
    :return: A histogram of the samples as a dictionary with the values as keys and counts as values.
    """
    # Check input
    if not isinstance(values, list):
        raise ValueError("values must be a list")
    if not isinstance(weights, list):
        raise ValueError("weights must be a list")
    if len(values) != len(weights):
        raise ValueError("values and weights must have the same length")
    if not isinstance(n_samples, int):
        raise ValueError("n_samples must be an integer")
    if n_samples < 0:
        raise ValueError("n_samples must be non-negative")

    # Generate samples
    samples = []
    for i in range(n_samples):
        sample = random.choices(values, weights=weights, k=1)[0]
        samples.append(sample)

    # Create histogram
    histogram = Counter(samples)

    return histogram
values = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.4, 0.5]
n_samples = 1000