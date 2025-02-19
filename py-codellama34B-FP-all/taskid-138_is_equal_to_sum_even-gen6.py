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

    # 1. all numbers are even
    # 2. sum of numbers is n
    # 3. numbers are distinct
    # 4. there are 4 numbers
    numbers = []
    for i in range(1, n):
        if i % 2 == 0:
            numbers.append(i)
    for i in range(1, n):
        if i % 2 == 0:
            numbers.append(i)
    for i in range(1, n):
        if i % 2 == 0:
            numbers.append(i)
    for i in range(1, n):
        if i % 2 == 0:
            numbers.append(i)
    return sum(numbers) == n
