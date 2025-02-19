from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    # Keep track of the numbers we've seen so far.
    seen = set()
    # The result we're building up.
    result = []

    for num in numbers:
        # Have we seen this number before?
        if num not in seen:
            # No, we haven't seen it before. Add it to both lists.
            result.append(num)
            seen.add(num)

    return result
