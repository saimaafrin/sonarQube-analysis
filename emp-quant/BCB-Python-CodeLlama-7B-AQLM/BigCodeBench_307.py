import seaborn as sns
import matplotlib.pyplot as plt
import random
def task_func(list_of_lists, seed=0):
    """
    Create a histogram from the data in a list of lists. If any sublist is empty, 
    it will be filled with 5 random integers ranging from 0 to 100 (both inclusive)
    The histogram will then be constructed using the combined data from all sublists.
    
    Parameters:
    list_of_lists (list): A list containing multiple sublists with integers.
    seed (int, Optional): Seed value for random number generation. Default is 0.
    
    Returns:
    matplotlib.axes._axes.Axes: The histogram plot object.
    
    Requirements:
    - random
    - seaborn
    - matplotlib.pyplot
    
    Example:
    >>> plot = task_func([[1, 2, 3], [], [4, 5, 6]])
    >>> type(plot)
    <class 'matplotlib.axes._axes.Axes'>
    """
    random.seed(seed)
    sns.set()
    plt.figure(figsize=(10, 5))
    plt.title("Histogram")
    plt.xlabel("Value")
    plt.ylabel("Frequency")
    plt.xticks(range(0, 101, 10))
    plt.yticks(range(0, 11, 1))
    plt.grid(True)
    for sublist in list_of_lists:
        if len(sublist) == 0:
            sublist = [random.randint(0, 100) for _ in range(5)]
        plt.hist(sublist, bins=10, density=True, alpha=0.5)
    return plt.gca()