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

    # The function is to make the pile in the format of
    # level 1: 3
    # level 2: 5
    # level 3: 7
    # level 4: 9
    # ...

    # Since the stones in the first level is given, we can start from there
    pile = [n]

    # Now we iterate through each level
    # Since we know the first level is 3, we start from i=2
    # i represents the level
    for i in range(2, n):
        # We check if n is odd or even
        if n % 2 == 0:
            # If n is even, the next level will have n + 2 stones
            pile.append(n + 2)
        else:
            # If n is odd, the next level will have n + 1 stones
            pile.append(n + 1)
        # We update the value of n to be the next level's number of stones
        n = pile[-1]
    
    return pile
