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


    def is_even(num: int) -> bool:
        return num % 2 == 0

    count_even_sum = 0

    for i in range(1, int(n ** 0.5) + 1):
        for j in range(i, int(n ** 0.5) + 1):
            for k in range(j, int(n ** 0.5) + 1):
                for m in range(k, int(n ** 0.5) + 1):
                    if i + j + k + m == n:
                        if is_even(i) and is_even(j) and is_even(k) and is_even(m):
                            count_even_sum += 1
    if count_even_sum == 1:
        return True
    return False
