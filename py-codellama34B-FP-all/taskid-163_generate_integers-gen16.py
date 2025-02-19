from typing import List

def generate_integers(a: int, b: int) -> List[int]:
    """
    Given two positive integers a and b, return the even digits between a
    and b, in ascending order.

    For example:
    >>> generate_integers(2, 8)
    [2, 4, 6, 8]
    >>> generate_integers(8, 2)
    [2, 4, 6, 8]
    >>> generate_integers(10, 14)
    []
    """

    # YOUR CODE HERE
    list_of_digits = []
    if a > b:
        for num in range(b, a + 1):
            str_num = str(num)
            for digit in str_num:
                if int(digit) % 2 == 0:
                    list_of_digits.append(int(digit))
        return list(set(list_of_digits))
    else:
        for num in range(a, b + 1):
            str_num = str(num)
            for digit in str_num:
                if int(digit) % 2 == 0:
                    list_of_digits.append(int(digit))
        return list(set(list_of_digits))
