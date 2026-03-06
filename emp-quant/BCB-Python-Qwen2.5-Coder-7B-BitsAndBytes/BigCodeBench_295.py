
import itertools
import statistics

# Refined function after importing required libraries
def task_func(elements, subset_size):
    # Generate all possible subsets of the given size
    subsets = list(itertools.combinations(elements, subset_size))
    
    # Calculate the sum of each subset
    subset_sums = [sum(subset) for subset in subsets]
    
    # Calculate mean, median, and mode of the subset sums
    mean_value = statistics.mean(subset_sums)
    median_value = statistics.median(subset_sums)
    mode_value = statistics.mode(subset_sums)
    
    # Return the results as a dictionary
    return {
        'mean': mean_value,
        'median': median_value,
        'mode': mode_value
    }