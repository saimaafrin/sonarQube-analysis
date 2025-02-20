def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    # Check the number of digits in 'n'.
    if n < 1:
        return 0

    # Set the count of numbers of 'n' digits that start or end with 1 to 0.
    count = 0

    # Generate the numbers of 'n' digits that start or end with 1.
    for i in range(1, 10**n):
        # Check if the number 'i' ends with 1.
        if str(i)[-1] == "1":
            count += 1

    # Return the count of numbers of 'n' digits that start or end with 1.
    return count
