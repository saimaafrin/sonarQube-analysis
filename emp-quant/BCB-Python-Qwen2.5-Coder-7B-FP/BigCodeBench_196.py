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
    
    random.seed(seed)
    random_numbers = [random.randint(0, range_limit - 1) for _ in range(length)]
    random_numbers.sort()
    
    sns.set(style="whitegrid")
    ax = sns.histplot(random_numbers, kde=False)
    plt.show()
    
    return ax, random_numbers