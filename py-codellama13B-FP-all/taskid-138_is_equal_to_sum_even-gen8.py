def is_equal_to_sum_even(n: int) -> bool:
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    >>> is_equal_to_sum_even(4)
    False
    >>> is_equal_to_sum_even(6)
    False
    >>> is_equal_to_sum_even(8)
    True
    """


    # 1. Check for even numbers
    if n % 2 == 1:
        return False

    # 2. Calculate the maximum number of even numbers
    max_even = n / 2
    if max_even < 4:
        return False

    # 3. Calculate the sum of the even numbers
    sum_even = 0
    for i in range(1, int(max_even / 2) + 1):
        sum_even += 2 * i

    # 4. Check if the sum is equal to the given number
    return sum_even == n
