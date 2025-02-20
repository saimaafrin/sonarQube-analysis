from typing import Tuple

def even_odd_palindrome(n: int) -> Tuple[int, int]:
    """
    Given a positive integer n, return a tuple that has the number of even and odd
    integer palindromes that fall within the range(1, n), inclusive.

    Example 1:

    >>> even_odd_palindrome(3)
    (1, 2)
        Explanation:
        Integer palindrome are 1, 2, 3. one of them is even, and two of them are odd.

    Example 2:

    >>> even_odd_palindrome(12)
    (4, 6)
        Explanation:
        Integer palindrome are 1, 2, 3, 4, 5, 6, 7, 8, 9, 11. four of them are even, and 6 of them are odd.

    Note:
        1. 1 <= n <= 10^3
        2. returned tuple has the number of even and odd integer palindromes respectively.
    """


    # Solution 1
    # O(n) time | O(1) space
    count_even = 0
    count_odd = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)

    # Solution 2
    # O(1) time | O(1) space
    return ((n // 2) + (n % 2), n // 2)

    # Solution 3
    # O(1) time | O(1) space
    count_even = n // 2
    count_odd = n // 2
    if n % 2 == 1:
        count_odd += 1
    return (count_even, count_odd)

    # Solution 4
    # O(1) time | O(1) space
    count_even = n // 2 + (n % 2)
    count_odd = n // 2
    return (count_even, count_odd)

    # Solution 5
    # O(1) time | O(1) space
    return ((n + 1) // 2, n // 2)
