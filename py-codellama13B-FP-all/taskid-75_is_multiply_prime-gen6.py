def is_multiply_prime(a: int) -> bool:
    """Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100. 
    Example:
    >>> is_multiply_prime(30)
    True
    30 = 2 * 3 * 5
    """

    # 1. Create a dictionary to keep track of all the prime numbers below 100
    primes = {2: True, 3: True, 5: True, 7: True}

    # 2. Define a function that checks if a given number is divisible by any of the prime numbers
    def is_divisible(number: int) -> bool:
        for prime in primes:
            if number % prime == 0:
                return True
        return False

    # 3. Iterate through all the numbers below 100 and check if they are divisible by any of the prime numbers
    for i in range(2, 100):
        # 3.1. If the current number is divisible by any of the prime numbers, mark it as False in the primes dictionary
        if is_divisible(i):
            primes[i] = False

    # 4. Return the result based on the values of the dictionary
    return a % 2 == 0 and primes[a]
