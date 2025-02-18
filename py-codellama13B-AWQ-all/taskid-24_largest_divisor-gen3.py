def largest_divisor(n: int) -> int:
    """ For a given number n, find the largest number that divides n evenly, smaller than n
    >>> largest_divisor(15)
    5
    """

    # if n is 1, then there is no divisor other than 1
    if n == 1:
        return 1
    
    # If the number is even, then the largest divisor will be 2
    if n % 2 == 0:
        return 2
    
    # If n is odd, then the largest divisor will be n - 1, provided that n - 1 is an even number
    if n - 1 % 2 == 0:
        return n - 1
    
    # If the largest divisor is not found, then return the value of n
    return n
