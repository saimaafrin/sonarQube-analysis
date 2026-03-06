
import numpy as np
from collections import Counter

def task_func(list_of_tuples):
    # Extract numeric values and categories from the list of tuples
    values = [item[0] for item in list_of_tuples]
    categories = [item[1] for item in list_of_tuples]
    
    # Calculate the sum of numeric values
    total_sum = np.sum(values)
    
    # Count the occurrences of each category
    category_counts = dict(Counter(categories))
    
    # Return the result as a tuple
    return (total_sum, category_counts)