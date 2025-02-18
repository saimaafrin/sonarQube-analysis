def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # The number of 1-digit positive integers starting with 1 is 9,
    # and the number of 1-digit positive integers ending with 1 is also 9.
    # If we want to check if the number is between 10 and 99,
    # we can use the built-in sum function to count the number of 1s
    # in a range of numbers between 10 and 99.
    if n == 1:
        return 9
    else:
        return sum(1 for i in range(10, 100) if str(i).count('1') == 1)
