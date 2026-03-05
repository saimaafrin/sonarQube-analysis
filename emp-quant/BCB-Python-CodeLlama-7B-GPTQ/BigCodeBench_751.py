import random
from collections import Counter
def task_func(values, weights, n_samples):
    """
    Sample random numbers based on a given weighted distribution and return a histogram of the samples.
    :param values: A list of values in the weighted distribution.
    :param weights: A list of weights for each value in the weighted distribution.
    :param n_samples: The number of samples to draw from the weighted distribution.
    :return: A histogram as a dictionary with the values as keys and counts as values.
    """
    histogram = Counter()
    for _ in range(n_samples):
        sample = random.choices(values, weights=weights, k=1)[0]
        histogram[sample] += 1
    return histogram
values = [1, 2, 3, 4, 5]
weights = [0.1, 0.2, 0.3, 0.4, 0.1]
n_samples = 1000