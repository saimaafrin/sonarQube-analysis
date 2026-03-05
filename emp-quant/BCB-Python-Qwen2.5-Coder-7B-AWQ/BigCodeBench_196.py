import random
import seaborn as sns
import numpy as np
from matplotlib import pyplot as plt
def task_func(length, range_limit=100, seed=0):
    """
    Generates a list of random numbers, sorts them, and plots a histogram using seaborn.
    
    Parameters:
    - length: int, the number of random numbers to generate.
    - range_limit: int, the upper limit for the range of random numbers (exclusive).
    - seed: int, the seed for the random number generator for reproducibility.
    
    Returns:
    - Tuple[matplotlib.axes._axes.Axes, List[int]]: The axes object with the plot and the list of random numbers.
    
    Raises:
    - ValueError: If range_limit is less than or equal to 1.
    """
    if range_limit <= 1:
        raise ValueError("range_limit must be greater than 1")
    
    # Set the seed for reproducibility
    random.seed(seed)
    
    # Generate a list of random numbers
    random_numbers = [random.randint(0, range_limit) for _ in range(length)]
    
    # Sort the list of random numbers
    sorted_numbers = sorted(random_numbers)
    
    # Create a histogram using seaborn
    axes = sns.histplot(sorted_numbers, kde=False)
    
    # Set the title and labels
    axes.set_title('Histogram of Random Numbers')
    axes.set_xlabel('Number')
    axes.set_ylabel('Frequency')
    
    return axes, sorted_numbers