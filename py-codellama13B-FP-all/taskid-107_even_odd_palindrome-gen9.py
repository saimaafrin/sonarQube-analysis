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

    # find the digits of n
    digits = []
    while n:
        digits.append(n % 10)
        n //= 10
    # find the reverse of the digits
    reverse_digits = []
    for digit in digits:
        reverse_digits.append(digit)
    # find the length of the digits
    length = len(digits)
    # initialize the number of even and odd palindromes
    even_palindrome, odd_palindrome = 0, 0
    # find the even palindromes
    for i in range(length):
        # check if the digit is even
        if digits[i] % 2 == 0:
            # check if the digit is the same as the digit at the reverse index
            if digits[i] == reverse_digits[length - 1 - i]:
                even_palindrome += 1
    # find the odd palindromes
    for i in range(length):
        # check if the digit is odd
        if digits[i] % 2 == 1:
            # check if the digit is the same as the digit at the reverse index
            if digits[i] == reverse_digits[length - 1 - i]:
                odd_palindrome += 1
    return even_palindrome, odd_palindrome
