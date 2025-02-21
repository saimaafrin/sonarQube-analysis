from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    if len(numbers) == 0:
        return (0, 1)
    else:
        # The first element of the tuple (sum) should equal to the sum of all elements of the list.
        # The second element (product) should equal to the product of all elements of the list.
        return (sum(numbers), reduce(lambda x, y: x * y, numbers))
