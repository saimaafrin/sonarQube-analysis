def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    # Initialize count for 1-digit numbers
    count = 0

    # Iterate through all possible 2-digit numbers
    for i in range(10):
        # Skip numbers that don't end in 1
        if i % 10 != 1:
            continue

        # Increment count for each 2-digit number that ends in 1
        count += n // 10

    # Add the number of 1-digit numbers
    count += n

    return count
