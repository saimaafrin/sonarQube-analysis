import collections
from itertools import zip_longest
from random import choices
def task_func(l1, l2, K=10):
    """
    Combine two lists by alternating their elements, even if they are of different lengths. Elements from the longer list without a counterpart in the shorter one will be included on their own. Then, create a random sample of size K from the combined list, and calculate the frequency of each element in the sample.
    """
    # Combine the two lists by alternating their elements
    combined_list = [element for element in zip_longest(l1, l2)]

    # Create a random sample of size K from the combined list
    sample = choices(combined_list, k=K)

    # Count the frequency of each element in the sample
    counter = collections.Counter(sample)

    return counter
l1 = [1, 2, 3]
l2 = [4, 5, 6, 7]
K = 5