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


    pile = [n]

    # This is a hint, not the solution.
    # It will be hard to find the pattern without some help.
    # The pattern is:
    #
    #     Next stone # | Pattern
    #     ------------ | ----------------------
    #                1 | 3, 5, 7, ..., 2n + 1
    #                2 | 4, 6, 8, ..., 2n + 2
    #                3 | 3, 5, 7, ..., 2n + 1
    #                4 | 4, 6, 8, ..., 2n + 2
    #                5 | 3, 5, 7, ..., 2n + 1
    #                6 | 4, 6, 8, ..., 2n + 2
    #                7 | 3, 5, 7, ..., 2n + 1
    #                ...
    #
    # The pattern repeats every 4 stone numbers.
    # Can you figure out a way to use this pattern to find the solution?

    return pile
