def largest_prime_factor(n: int) -> int:
    """Return the largest prime factor of n. Assume n > 1 and is not a prime.
    >>> largest_prime_factor(13195)
    29
    >>> largest_prime_factor(2048)
    2
    """


    # Initialize a variable to hold the largest prime factor.
    largest_prime = 0

    # Initialize a variable to iterate through the potential factors of n.
    potential_factor = 2

    # Iterate through the potential factors of n,
    # testing whether each is a factor of n.
    while potential_factor <= n:

        # If the current potential factor is a factor of n,
        # then test whether it is prime.
        if n % potential_factor == 0:

            # If the current potential factor is prime,
            # then update the largest prime factor.
            if is_prime(potential_factor):
                largest_prime = potential_factor

        # Increment the potential factor to test the next factor of n.
        potential_factor += 1

    # Return the largest prime factor.
    return largest_prime
