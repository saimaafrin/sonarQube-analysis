
import itertools
import statistics

def task_func(elements, subset_size):
    # Generate all subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sums of the subsets
    subset_sums = [sum(subset) for subset in subsets]
    
    # Calculate the mean, median, and mode of the subset sums
    mean = statistics.mean(subset_sums)
    median = statistics.median(subset_sums)
    mode = statistics.mode(subset_sums)
    
    # Return the results as a dictionary
    return {
        'mean': mean,
        'median': median,
        'mode': mode
    }