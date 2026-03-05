
import numpy as np
from collections import Counter

def task_func(list_of_tuples):
    # Calculate the sum of all numeric values
    sum_of_values = np.sum(list_of_tuples)

    # Count the occurrences of each category
    category_counts = Counter(list_of_tuples)

    return (sum_of_values, category_counts)