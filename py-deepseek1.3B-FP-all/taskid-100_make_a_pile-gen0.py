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


    # Calculate initial level
    level = n if n % 2 == 1 else n - 1
    pile = [level]
    
    # Calculate the number of stones in each subsequent level
    while level + n <= n * 2:
        level += 2 if level % 2 == 0 else 1
        pile.append(level)
    
    return pile
