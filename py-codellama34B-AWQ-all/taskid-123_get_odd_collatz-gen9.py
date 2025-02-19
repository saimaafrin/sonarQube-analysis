from typing import List

def get_odd_collatz(n: int) -> List[int]:
    """
    Given a positive integer n, return a sorted list that has the odd numbers in collatz sequence.

    The Collatz conjecture is a conjecture in mathematics that concerns a sequence defined
    as follows: start with any positive integer n. Then each term is obtained from the 
    previous term as follows: if the previous term is even, the next term is one half of 
    the previous term. If the previous term is odd, the next term is 3 times the previous
    term plus 1. The conjecture is that no matter what value of n, the sequence will always reach 1.

    Note: 
        1. Collatz(1) is [1].
        2. returned list sorted in increasing order.

    For example:
    get_odd_collatz(5) returns [1, 5] # The collatz sequence for 5 is [5, 16, 8, 4, 2, 1], so the odd numbers are only 1, and 5.
    >>> get_odd_collatz(5)
    [1, 5]
    """

    assert n > 0, "n should be a positive integer."

    # use list to hold odd numbers
    odd_list = []

    # use a while loop to get the odd number
    while n > 1:
        # when n is even
        if n % 2 == 0:
            n = n // 2
        # when n is odd
        else:
            n = 3 * n + 1
            # if odd number found, add to the list
            odd_list.append(n)
    
    # return the sorted odd list
    return sorted(odd_list)
