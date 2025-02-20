def x_or_y(n: int, x: int, y: int) -> int:
    """A simple program which should return the value of x if n is 
    a prime number and should return the value of y otherwise.

    Examples:
    >>> x_or_y(7, 34, 12)
    34
    >>> x_or_y(15, 8, 5)
    5
    
    """

    # A variable to store the result
    result = None

    # Check if n is a prime number or not
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                # If n is divisible by any number other than 1 and itself, it is not prime
                result = y
                break
        else:
            # If n is not divisible by any number, it is prime
            result = x
    else:
        # If the number is less than or equal to 1, it is not prime
        result = y

    return result
