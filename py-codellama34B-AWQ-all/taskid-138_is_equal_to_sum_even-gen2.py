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

    even_nums = []
    for i in range(1, n):
        if i % 2 == 0:
            even_nums.append(i)
    if len(even_nums) != 4:
        return False
    return sum(even_nums) == n
