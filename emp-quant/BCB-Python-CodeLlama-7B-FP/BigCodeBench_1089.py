import numpy as np
from collections import Counter
def task_func(list_of_tuples):
    """
    Computes the sum of numeric values and counts the occurrences of categories in a list of tuples.
    Each tuple in the input list contains a numeric value and a category.
    This function calculates the sum of all the numeric values and also counts how many times each category appears in the list.
    The function should output with:
        tuple: A 2-element tuple where the first element is the sum of the numeric values, and the
        second element is a dictionary with categories as keys and their counts as values.
    """
    # Initialize variables
    sum_of_values = 0
    category_counts = Counter()

    # Iterate over the list of tuples
    for value, category in list_of_tuples:
        # Add the value to the sum
        sum_of_values += value

        # Increment the count for the category
        category_counts[category] += 1

    # Return the tuple
    return (sum_of_values, category_counts)
list_of_tuples = [
    (1, "A"),
    (2, "B"),
    (3, "A"),
    (4, "B"),
    (5, "A"),
    (6, "B"),
]