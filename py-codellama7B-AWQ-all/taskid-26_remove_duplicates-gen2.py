from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """


    # Step 1: Make a dict of counts of each number in the list.
    counts = {}
    for num in numbers:
        counts[num] = counts.get(num, 0) + 1
    # Step 2: Walk through the input list and remove elements
    # that have count > 1
    result = []
    for num in numbers:
        if counts[num] > 1:
            continue
        result.append(num)
    return result
