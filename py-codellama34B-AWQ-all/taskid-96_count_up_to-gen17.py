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


    # The basic idea is to keep a list of all the prime numbers we've found so far.
    # Whenever we find a new prime number, we add it to the list.
    prime_numbers = []

    # There are no prime numbers less than 0, so if n is 0 or less,
    # we can return an empty list right away.
    if n <= 0:
        return prime_numbers

    # We start at 2, which is the smallest prime number.
    # We keep checking numbers until we reach the number n.
    for num in range(2, n+1):
        # We assume that the number is prime until we find out otherwise.
        # This is the "optimistic" thing to do.
        is_prime = True

        # To check if a number is prime, we iterate through all the prime numbers
        # we've found so far and see if any of them divide evenly into num.
        # If none of them do, then num is prime.
        for prime in prime_numbers:
            if num % prime == 0:
                # If we find a factor, we know the number is not prime,
                # so we can stop looking.
                is_prime = False
                break

        # If we didn't find any factors, then num is prime,
        # so we add it to the list of prime numbers.
        if is_prime:
            prime_numbers.append(num)

    return prime_numbers
