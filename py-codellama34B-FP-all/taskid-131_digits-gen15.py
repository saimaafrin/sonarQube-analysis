def digits(n: int) -> int:
    """Given a positive integer n, return the product of the odd digits.
    Return 0 if all digits are even.
    For example:
    >>> digits(1)
    1
    >>> digits(4)
    0
    >>> digits(235)
    15
    """


    return int(
        "".join(
            [
                str(n % 10)
                for n in range(1, int(math.log10(n)) + 1)
                if int(str(n)[-1]) % 2
            ]
        )
    )
