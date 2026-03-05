import collections
from itertools import zip_longest
from random import choices
def task_func(l1, l2, K=10):
    """
    Combine two lists by alternating their elements, even if they are of different lengths. Elements from the longer list without a counterpart in the shorter one will be included on their own. Then, create a random sample of size K from the combined list, and calculate the frequency of each element in the sample.
    """
    # Combine the two lists by alternating their elements
    combined_list = []
    for i, j in zip_longest(l1, l2):
        if i is not None:
            combined_list.append(i)
        if j is not None:
            combined_list.append(j)

    # Create a random sample of size K from the combined list
    sample = choices(combined_list, k=K)

    # Calculate the frequency of each element in the sample
    counter = collections.Counter(sample)

    return counter
l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]