from typing import List, Tuple

def sum_product(numbers: List[int]) -> Tuple[int, int]:
    """ For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
    Empty sum should be equal to 0 and empty product should be equal to 1.
    >>> sum_product([])
    (0, 1)
    >>> sum_product([1, 2, 3, 4])
    (10, 24)
    """

    sum_numbers = sum(numbers)
    product_numbers = 1
    if sum_numbers == 0:
        return (0, 1)
    else:
        for num in numbers:
            product_numbers *= num
        return (sum_numbers, product_numbers)
