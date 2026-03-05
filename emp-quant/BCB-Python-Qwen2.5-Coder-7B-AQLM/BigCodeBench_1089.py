
import numpy as np
from collections import Counter

def task_func(list_of_tuples):
    # Initialize sum and counter
    total_sum = 0
    category_counter = Counter()
    
    # Iterate through each tuple in the list
    for value, category in list_of_tuples:
        # Add the numeric value to the total sum
        total_sum += value
        # Increment the count for the category
        category_counter[category] += 1
    
    # Create the result tuple
    result = (total_sum, dict(category_counter))
    
    return result