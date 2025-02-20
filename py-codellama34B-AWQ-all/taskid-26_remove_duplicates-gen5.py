from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """


    def remove_duplicates_helper(numbers: List[int], index: int) -> int:
        """ Recursive helper method that removes duplicates from a list of integers.
        >>> remove_duplicates_helper([1, 2, 3, 2, 4], 0)
        3
        """
        if index >= len(numbers):
            return 0
        else:
            num = numbers[index]
            if numbers.index(num) != index:
                numbers.pop(index)
                return remove_duplicates_helper(numbers, index)
            else:
                return 1 + remove_duplicates_helper(numbers, index+1)

    remove_duplicates_helper(numbers, 0)
    return numbers
