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

    if not 1 <= n <= 1000:
        raise ValueError("1 <= n <= 1000")

    even_count, odd_count = 0, 0
    for i in range(1, n+1):
        # i has 2 digits, so i // 100 == 0
        # i has 3 digits, so i // 100 != 0
        if i // 100 != 0:
            # i has 3 digits
            # case 1: aaa
            # case 2: aba
            # case 3: aab
            # case 4: aca
            # case 5: acb
            # case 6: aac
            # case 7: bab
            # case 8: bcb
            # case 9: bac
            # case 10: bba
            # case 11: bcb
            # case 12: bac
            # case 13: bba
            # case 14: bcb
            # case 15: bab
            # case 16: bcb
            # case 17: bac
            # case 18: bba
            # case 19: bcb
            # case 20: bac
            # case 21: bba
            # case 22: bcb
            # case 23: bab
            # case 24: bcb
            # case 25: bac
            # case 26: bba
            # case 27: bcb
            # case 28: bac
            # case 29: bba
            # case 30: bcb
            # case 31: bab
            # case 32: bcb
            # case 33: bac
            # case 34: bba
            # case 35: bcb
            # case 36: bac
            # case 37: bba
            # case 38: bcb
            # case 39: bac
            # case 40: bba
            # case 41: bcb
            # case 42: bab
            # case 43: bcb
            # case 44: bac
            # case 45: bba
            # case 46: bcb
            # case 47: bac
            # case 48: bba
            # case 49: bcb
            # case 50: bac
            # case 51: bba
            # case 52: bcb
            # case 53: bab
            # case 54: bcb
            # case 55: bac
            # case 56: bba
            # case 57: bcb
            # case 58: bac
            # case 59: bba
            # case 60: bcb
            # case 61: bab
            # case 62: bcb
            # case 63: bac
            # case 64: bba
            # case 65: b
