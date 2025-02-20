def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # 10^n - 10^(n-1) is the number of n-digit positive integers
    # that end in 1.
    #
    # 10^(n-1) - 10^(n-2) is the number of n-digit positive integers
    # that start in 1.
    #
    # Add the two together to get the total number of n-digit positive
    # integers that start or end in 1.
    return (10 ** n - 10 ** (n - 1)) + (10 ** (n - 1) - 10 ** (n - 2))
