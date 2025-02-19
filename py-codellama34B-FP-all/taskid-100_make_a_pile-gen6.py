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

    # Create a result list to store the number of stones at each level.
    result = []
    # Add the number of stones in the first level to the result list.
    result.append(n)

    # Loop until the number of stones in the level is 1.
    while n != 1:
        # Check if n is odd.
        if n % 2 == 1:
            # Add the next odd number to the result list.
            result.append(n + 2)
            # Add the next odd number to the current level number.
            n += 2
        # Check if n is even.
        elif n % 2 == 0:
            # Add the next even number to the result list.
            result.append(n + 1)
            # Add the next even number to the current level number.
            n += 1

    # Return the number of stones at each level.
    return result
