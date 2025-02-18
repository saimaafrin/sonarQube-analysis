def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Convert to binary
    binary = bin(n)[2:]

    # Count the number of digits that start with 1
    count = 0
    for digit in binary:
        if digit == "1":
            count += 1

    return count
