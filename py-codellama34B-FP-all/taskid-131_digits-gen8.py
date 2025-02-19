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
            map(
                lambda x: x[1] if x[0] % 2 != 0 else "",
                map(lambda x: (x[0], x[1]), enumerate(str(n)))
            )
        )
    )
