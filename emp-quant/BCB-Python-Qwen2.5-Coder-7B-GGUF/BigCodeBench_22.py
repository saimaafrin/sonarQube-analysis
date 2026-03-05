
import collections
from itertools import zip_longest
from random import choices

def task_func(l1, l2, K=10):
    # Combine two lists by alternating their elements
    combined = [item for sublist in zip_longest(l1, l2, fillvalue=None) for item in sublist if item is not None]
    
    # Create a random sample of size K from the combined list
    sample = choices(combined, k=K)
    
    # Calculate the frequency of each element in the sample
    frequency = collections.Counter(sample)
    
    return frequency