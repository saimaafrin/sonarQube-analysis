import itertools
import statistics
def task_func(elements, subset_size):
    """
    Generate all subsets of a given size from a tuple and calculate the mean, median, and mode of the sums of the subsets.

    Args:
        elements (tuple): A tuple of numbers from which subsets will be generated.
        subset_size (int): The size of the subsets to be generated.

    Returns:
        dict: A dictionary with the mean, median, and mode of the sums of the subsets.
    """
    subsets = list(itertools.combinations(elements, subset_size))
    sums = [sum(subset) for subset in subsets]
    mean = statistics.mean(sums)
    median = statistics.median(sums)
    mode = statistics.mode(sums)
    return {'mean': mean, 'median': median, 'mode': mode}
elements = (1, 2, 3, 4, 5)
subset_size = 2