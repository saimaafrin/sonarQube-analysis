def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    if n < 0 or n > 10:
        raise ValueError('n must be between 0 and 10')

    starts = 0
    ends = 0

    for i in range(1, 10 ** n):
        number = str(i)
        if number[0] == '1' or number[-1] == '1':
            if number[0] == '1':
                starts += 1
            elif number[-1] == '1':
                ends += 1
            else:
                raise ValueError('Unexpected number encountered')

    return starts + ends
