
import collections
from itertools import zip_longest
from random import choices

def task_func(l1, l2, K=10):
    # Combine the lists by alternating their elements
    combined = []
    for x, y in zip_longest(l1, l2, fillvalue=None):
        combined.append(x)
        combined.append(y)
    
    # Filter out None values that were added during the combination
    combined = [item for item in combined if item is not None]
    
    # Create a random sample of size K from the combined list
    sample = choices(combined, k=K)
    
    # Calculate the frequency of each element in the sample
    frequency = collections.Counter(sample)
    
    return frequency