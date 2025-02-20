def is_equal_to_sum_even(n: int) -> bool:
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    >>> is_equal_to_sum_even(4)
    False
    >>> is_equal_to_sum_even(6)
    False
    >>> is_equal_to_sum_even(8)
    True
    """

    # check if the given number is a positive even number
    if n % 2 != 0 or n <= 0:
        return False

    # calculate the square root of the given number
    sqrt_n = int(math.sqrt(n))

    # iterate over the divisors of the given number from 2 up to the square root of the given number
    for divisor in range(2, sqrt_n + 1):
        # check if the divisor is an even number
        if divisor % 2 == 0:
            # calculate the sum of the divisors
            divisor_sum = divisor + (n // divisor)
            # check if the sum of the divisors is equal to the given number
            if divisor_sum == n:
                return True

    # if the given number cannot be written as the sum of exactly 4 positive even numbers
    return False
