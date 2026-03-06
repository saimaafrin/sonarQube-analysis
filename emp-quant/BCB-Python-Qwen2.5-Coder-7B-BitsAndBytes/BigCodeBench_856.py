
from functools import reduce
from itertools import combinations
import numpy as np

def task_func(shape=(3, 3), low=1, high=10, seed=None):
    if high <= low:
        raise ValueError("high must be greater than low")
    
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate the matrix with random integers between low and high
    matrix = np.random.randint(low, high, size=shape)
    
    # Flatten the matrix to get a list of all elements
    flat_list = matrix.flatten()
    
    # Generate all possible pairs using combinations
    pairs = combinations(flat_list, 2)
    
    # Calculate the product of each pair
    products = (a * b for a, b in pairs)
    
    # Sum up all the products
    total_sum = reduce(lambda x, y: x + y, products)
    
    return total_sum, matrix