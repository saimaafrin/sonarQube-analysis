from typing import List

def remove_duplicates(numbers: List[int]) -> List[int]:
    """ From a list of integers, remove all elements that occur more than once.
    Keep order of elements left the same as in the input.
    >>> remove_duplicates([1, 2, 3, 2, 4])
    [1, 3, 4]
    """

    unique_nums = set()
    unique_list = []
    for num in numbers:
        if num not in unique_nums:
            unique_list.append(num)
            unique_nums.add(num)

    return unique_list
