def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Initialize the count variable
    count = 0

    # Check for the ones that start with 1
    for i in range(10 ** (n - 1), 10 ** n):
        if str(i)[0] == '1' or str(i)[-1] == '1':
            count += 1

    # Return the count
    return count
