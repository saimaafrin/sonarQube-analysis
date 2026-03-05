
import numpy as np
from collections import Counter

def task_func(list_of_tuples):
    # Extract numeric values and categories
    numeric_values = [item[0] for item in list_of_tuples]
    categories = [item[1] for item in list_of_tuples]
    
    # Calculate the sum of numeric values
    sum_numeric_values = np.sum(numeric_values)
    
    # Count the occurrences of each category
    category_counts = Counter(categories)
    
    # Return the results as a tuple
    return (sum_numeric_values, dict(category_counts))