from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # Note: the function could be made much more efficient by using the
    # `unique_everseen` function from the `itertools` package.
    # However, this is left as an exercise to the reader.
    result = []
    for n in numbers:
        if n not in result:
            result.append(n)
    return result
