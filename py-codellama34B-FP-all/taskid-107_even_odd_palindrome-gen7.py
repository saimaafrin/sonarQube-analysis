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


    # 0. edge cases

    # 1. init variables
    even_count = 0
    odd_count = 0

    # 2. loop through range(1, n + 1)
    for i in range(1, n + 1):
        # 3. if i is palindrome
        if str(i) == str(i)[::-1]:
            # 4. if i is even
            if i % 2 == 0:
                # 5. increment even count
                even_count += 1
            # 6. else if i is odd
            else:
                # 7. increment odd count
                odd_count += 1

    # 8. return tuple(even count, odd count)
    return even_count, odd_count
