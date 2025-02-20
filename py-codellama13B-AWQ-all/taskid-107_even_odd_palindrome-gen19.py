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


    def __check(n: int) -> Tuple[bool, int]:
        """
        Checks if the given integer is a palindrome or not.
        """
        rev = 0
        temp = n

        while temp > 0:
            rev = (rev * 10) + temp % 10
            temp //= 10

        if n == rev:
            return (n % 2 == 0, n)
        else:
            return (n % 2 == 0, 0)

    even = 0
    odd = 0

    for i in range(1, n+1):
        res = __check(i)
        if res[0]:
            even += res[1]
        else:
            odd += res[1]

    return (even, odd)
