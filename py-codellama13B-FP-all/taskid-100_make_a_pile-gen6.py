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

    # pile = [n]
    # for i in range(1, n):
    #     if i % 2 == 0:
    #         pile.append(i + 2)
    #     else:
    #         pile.append(i + 1)
    # return pile
    return [n] + [n + 1 if i % 2 == 0 else n + 2 for i in range(1, n)]
