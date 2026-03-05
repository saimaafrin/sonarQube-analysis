
import numpy as np
from collections import Counter

def task_func(list_of_tuples):
    """
    Computes the sum of numeric values and counts the occurrences of categories in a list of tuples.
    Each tuple in the input list contains a numeric value and a category.
    This function calculates the sum of all the numeric values and also counts how many times each category appears in the list.
    """
    # Initialize the sum and the counter
    sum_of_values = 0
    counter = Counter()

    # Iterate over the tuples in the list
    for tuple in list_of_tuples:
        # Add the numeric value to the sum
        sum_of_values += tuple[0]

        # Increment the counter for the category
        counter[tuple[1]] += 1

    # Return the sum and the counter
    return (sum_of_values, counter)