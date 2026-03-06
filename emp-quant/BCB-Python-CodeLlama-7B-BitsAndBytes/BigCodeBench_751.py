
import random
from collections import Counter

def task_func(values, weights, n_samples):
    # Initialize the histogram
    histogram = Counter()

    # Generate n_samples random numbers based on the weighted distribution
    for _ in range(n_samples):
        # Select a random value based on the weights
        random_value = random.choices(values, weights=weights)[0]
        # Increment the count for the selected value in the histogram
        histogram[random_value] += 1

    return histogram

histogram = task_func(values, weights, n_samples)
print(histogram)