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

    # init the list
    collatz_list = []
    # init the number
    num = n

    # check the number
    if num == 1:
        return [1]

    # loop to get the odd numbers in collatz sequence
    while num != 1:
        # check if the number is odd
        if num % 2 != 0:
            collatz_list.append(num)
        # check if the number is even
        if num % 2 == 0:
            # get the number by half
            num = num / 2
            # check if the number is odd
            if num % 2 != 0:
                collatz_list.append(num)

    # return the sorted list
    return sorted(collatz_list)
