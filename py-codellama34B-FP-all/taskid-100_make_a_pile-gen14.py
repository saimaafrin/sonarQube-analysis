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

    result = []
    # Your code here
    # Remember that you can use
    #   result.append(item)
    # to add an item at the end of the result list
    # Good luck!

    if n == 0:
        return []
    result.append(n)
    if n % 2 == 0:
        while n > 0:
            result.append(n + 2)
            n += 2
        return result
    while n > 0:
        result.append(n + 1)
        n += 2
    return result
