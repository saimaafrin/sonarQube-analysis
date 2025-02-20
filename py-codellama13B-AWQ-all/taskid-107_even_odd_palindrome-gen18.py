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

    # 1. initialize the number of even and odd integer palindromes as 0
    even_count = 0
    odd_count = 0

    # 2. iterate over the range of 1 to n, inclusive
    for i in range(1, n + 1):
        # 3. compute the reverse of i
        reverse = 0
        temp = i

        # 4. iterate over temp, reverse the digits, and compute the reverse
        while temp > 0:
            reverse *= 10
            reverse += temp % 10
            temp //= 10

        # 5. if i and reverse are equal, i is an even integer palindrome
        #    else i is an odd integer palindrome
        if i == reverse:
            even_count += 1
        else:
            odd_count += 1

    # 6. return the number of even and odd integer palindromes
    return (even_count, odd_count)
