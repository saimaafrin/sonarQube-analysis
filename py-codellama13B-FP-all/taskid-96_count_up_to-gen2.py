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

    # Initialize a new empty list to contain the prime numbers
    prime_numbers = []

    # Iterate from 2 to n - 1
    for i in range(2, n):
        # Initialize a flag to represent whether the current number is prime
        is_prime = True

        # Iterate from 2 to the square root of i
        for j in range(2, int(i ** 0.5) + 1):
            # If i is divisible by j, it is not prime
            if i % j == 0:
                is_prime = False
                break

        # If the current number is prime, add it to the list of prime numbers
        if is_prime:
            prime_numbers.append(i)

    return prime_numbers
