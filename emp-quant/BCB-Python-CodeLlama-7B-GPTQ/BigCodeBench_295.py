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
    # Generate all subsets of the given size from the tuple
    subsets = itertools.combinations(elements, subset_size)

    # Calculate the mean, median, and mode of the sums of the subsets
    means = [statistics.mean(sum(subset)) for subset in subsets]
    medians = [statistics.median(sum(subset)) for subset in subsets]
    modes = [statistics.mode(sum(subset)) for subset in subsets]

    # Return the results as a dictionary
    return {
        "mean": means,
        "median": medians,
        "mode": modes
    }
elements = (1, 2, 3, 4, 5)
subset_size = 3