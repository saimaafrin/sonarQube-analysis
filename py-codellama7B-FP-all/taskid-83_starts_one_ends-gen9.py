def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    # Validate input.
    if n < 1:
        raise ValueError('n < 1')

    # Initialize result.
    result = 0

    # Iterate through all 1-digit numbers.
    for i in range(0, 10):

        # Skip if it doesn't start or end with 1.
        if i != 1 and i != 9:
            continue

        # Iterate through all n-1 digit numbers.
        for j in range(0, 10**(n-1)):

            # Skip if it doesn't start or end with 1.
            if i == 1 and j % 10 != 1:
                continue
            if i == 9 and j % 10 != 9:
                continue

            # Increment result.
            result += 1

    return result
