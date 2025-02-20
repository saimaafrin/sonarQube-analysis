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

    # Initialization
    pile: List[int] = [n]

    # Loop until the number of stones in the next level is bigger than n
    while pile[-1] <= n:
        pile.append(pile[-1] + 2 * (pile[-1] % 2) + 1)

    # Return the list without the last element, as the last element is bigger
    # than n
    return pile[:-1]
