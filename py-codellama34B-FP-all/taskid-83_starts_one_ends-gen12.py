def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Convert n to a string
    n = str(n)
    # Initialize a counter
    count = 0
    # Loop over each digit
    for i in range(1, len(n)+1):
        # If the digit starts or ends with 1, add 1 to the count
        if n[0] == '1' or n[-1] == '1':
            count += 1
    # Return the count
    return count
