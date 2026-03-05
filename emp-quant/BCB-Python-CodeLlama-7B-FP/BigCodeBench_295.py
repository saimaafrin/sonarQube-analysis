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
    sums = [sum(subset) for subset in subsets]
    mean = statistics.mean(sums)
    median = statistics.median(sums)
    mode = statistics.mode(sums)

    # Return the results as a dictionary
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
    }
elements = (1, 2, 3, 4, 5)
subset_size = 3