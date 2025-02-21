from typing import List

def make_a_pile(n: int) -> List[int]:
    """
    Given a positive integer n, you have to make a pile of n levels of stones.
    The first level has n stones.
    The number of stones in the next level is:
        - the next odd number if n is odd.
        - the next even number if n is even.
    Return the number of stones in each level in a list, where element at index
    i represents the number of stones in the level (i+1).

    Examples:
    >>> make_a_pile(3)
    [3, 5, 7]
    """

    if n <= 0:
        raise ValueError("Invalid input, n should be positive.")
    result = []
    current_level_size = n
    while current_level_size > 0:
        result.append(current_level_size)
        current_level_size = current_level_size + 1 if n % 2 == 0 else n // 2 + 1
    return result[::-1]
