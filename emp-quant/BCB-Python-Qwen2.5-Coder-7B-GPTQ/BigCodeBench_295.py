import itertools
import statistics
def task_func(elements, subset_size):
    # Generate all possible subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sum of each subset
    subset_sums = [sum(subset) for subset in subsets]
    
    # Calculate mean, median, and mode of the subset sums
    mean = statistics.mean(subset_sums)
    median = statistics.median(subset_sums)
    mode = statistics.mode(subset_sums)
    
    # Return the results in a dictionary
    return {
        'mean': mean,
        'median': median,
        'mode': mode
    }
elements = (1, 2, 3, 4)
subset_size = 2