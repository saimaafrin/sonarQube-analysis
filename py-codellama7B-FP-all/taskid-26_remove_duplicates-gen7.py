from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    result: List[int] = []
    seen: List[int] = []
    for n in numbers:
        if n not in seen:
            result.append(n)
            seen.append(n)
    return result
