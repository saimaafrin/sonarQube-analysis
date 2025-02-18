from typing import List

def count_up_to(n: int) -> List[int]:
    """Implement a function that takes an non-negative integer and returns an array of the first n
    integers that are prime numbers and less than n.
    for example:
    >>> count_up_to(5)
    [2, 3]
    >>> count_up_to(11)
    [2, 3, 5, 7]
    >>> count_up_to(0)
    []
    >>> count_up_to(20)
    [2, 3, 5, 7, 11, 13, 17, 19]
    >>> count_up_to(1)
    []
    >>> count_up_to(18)
    [2, 3, 5, 7, 11, 13, 17]
    """


    # If the input is 0 or negative, the function should return an empty array
    if n <= 0:
        return []

    # Initialize an array of zeros with the same length as the input
    prime_numbers = [False] * n
    prime_numbers[0] = True
    prime_numbers[1] = True

    # Iterate over the prime numbers (2 and 3) and mark their multiples as false
    for i in range(2, int(n**0.5) + 1):
        if prime_numbers[i]:
            for j in range(i*i, n, i):
                prime_numbers[j] = False

    return [i for i in range(n) if prime_numbers[i]]
