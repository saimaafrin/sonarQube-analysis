def starts_one_ends(n: int) -> int:
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """


    # Edge case: n is 1
    if n == 1:
        return 1

    # Edge case: n is 2
    if n == 2:
        return 9

    # Base case: n is greater than 2
    # Generate a range of n-digit positive integers
    range_nums = range(10**(n-1), 10**n)

    # Initialize a count for starting with 1
    count_start_with_1 = 0

    # Initialize a count for ending with 1
    count_end_with_1 = 0

    # Iterate through the range and increment the count if a number starts or ends with 1
    for i in range_nums:
        if str(i)[0] == "1":
            count_start_with_1 += 1
        elif str(i)[-1] == "1":
            count_end_with_1 += 1

    return count_start_with_1 + count_end_with_1
