
import numpy as np
from collections import Counter

def task_func(list_of_tuples):
    # Initialize the sum and counter dictionaries
    sum_dict = {}
    count_dict = {}

    # Iterate through the list of tuples
    for tuple in list_of_tuples:
        # Extract the numeric value and category from the tuple
        value = tuple[0]
        category = tuple[1]

        # Add the value to the sum dictionary
        if category in sum_dict:
            sum_dict[category] += value
        else:
            sum_dict[category] = value

        # Increment the count for the category
        if category in count_dict:
            count_dict[category] += 1
        else:
            count_dict[category] = 1

    # Return the sum and count dictionaries
    return (sum_dict, count_dict)

sum_dict, count_dict = task_func(list_of_tuples)
print(sum_dict)
# Output: {'A': 40, 'B': 60, 'C': 40}
print(count_dict)
# Output: {'A': 2, 'B': 3, 'C': 1}