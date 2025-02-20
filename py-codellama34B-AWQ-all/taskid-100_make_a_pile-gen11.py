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


    if n == 1:
        return [1]
    if n == 2:
        return [2, 3]

    stones: List[int] = []
    current_level = n

    while current_level > 1:
        if current_level % 2 == 0:
            current_level -= 1
        else:
            current_level += 1

        stones.append(current_level)

    stones.sort()
    return stones
