import numpy as np
from collections import Counter
def task_func(list_of_tuples):
    # Extract numeric values and categories from the list of tuples
    values = [item[0] for item in list_of_tuples]
    categories = [item[1] for item in list_of_tuples]
    
    # Calculate the sum of numeric values
    sum_values = np.sum(values)
    
    # Count the occurrences of each category
    category_counts = dict(Counter(categories))
    
    # Return the result as a tuple
    return (sum_values, category_counts)
list_of_tuples = [(1, 'apple'), (2, 'banana'), (3, 'apple'), (4, 'orange'), (5, 'banana')]