
import collections
from itertools import zip_longest
from random import choices

def task_func(l1, l2, K=10):
    # Combine the two lists by alternating their elements
    combined_list = [e1 if e1 is not None else e2 for e1, e2 in zip_longest(l1, l2)]

    # Create a random sample of size K from the combined list
    sample = choices(combined_list, K)

    # Calculate the frequency of each element in the sample
    counter = collections.Counter(sample)

    return counter