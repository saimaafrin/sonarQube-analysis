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

    even_numbers = []
    for i in range(1, n + 1):
        if i % 2 == 0:
            even_numbers.append(i)

    sum_even = []
    for i in range(len(even_numbers)):
        for j in range(i, len(even_numbers)):
            for k in range(j, len(even_numbers)):
                for l in range(k, len(even_numbers)):
                    if sum([even_numbers[i], even_numbers[j], even_numbers[k], even_numbers[l]]) == n:
                        sum_even.append(even_numbers[i])
                        sum_even.append(even_numbers[j])
                        sum_even.append(even_numbers[k])
                        sum_even.append(even_numbers[l])
                        break

    if len(sum_even) == 4:
        return True

    return False
