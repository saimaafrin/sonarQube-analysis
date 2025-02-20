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

    # edge cases
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    # initialize the counter
    counter_even = 0
    counter_odd = 0

    # loop through all the values
    for value in range(1, n + 1):
        # initialize the flag
        flag_palindrome = True

        # initialize the reversed value
        reversed_value = 0

        # loop through all the digits of the value
        for digit in reversed(str(value)):
            # update the reversed value
            reversed_value = reversed_value * 10 + int(digit)

            # check if the reversed value is equal to the value
            if reversed_value == value:
                # increment the counter
                if value % 2 == 0:
                    counter_even += 1
                else:
                    counter_odd += 1

                # set the flag
                flag_palindrome = False

                # break the loop
                break

        # check if the value is a palindrome
        if flag_palindrome:
            # increment the counter
            if value % 2 == 0:
                counter_even += 1
            else:
                counter_odd += 1

    # return the counter
    return counter_even, counter_odd
