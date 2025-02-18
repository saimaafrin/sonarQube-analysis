def fizz_buzz(n: int) -> int:
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
    >>> fizz_buzz(50)
    0
    >>> fizz_buzz(78)
    2
    >>> fizz_buzz(79)
    3
    """

    # check for edge case
    if n <= 0:
        return 0

    # set up the numbers and divisor
    numbers = range(1, n)
    divisor = 11

    # set up the fizz and buzz counter
    fizz = 0
    buzz = 0

    # iterate over the numbers
    for num in numbers:
        # increment fizz or buzz counter
        if num % divisor == 0:
            fizz += 1
        elif str(num).find('7') > 0:
            buzz += 1

    return fizz + buzz
