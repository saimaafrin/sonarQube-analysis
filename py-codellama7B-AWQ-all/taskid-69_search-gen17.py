from typing import List

def search(lst: List[int]) -> int:
    """
    You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    zero, and has a frequency greater than or equal to the value of the integer itself. 
    The frequency of an integer is the number of times it appears in the list.
    If no such a value exist, return -1.
    Examples:
    >>> search([4, 1, 2, 2, 3, 1])
    2
    >>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
    3
    >>> search([5, 5, 4, 4, 4])
    -1
    """


    # 1st solution
    # def search(lst: List[int]) -> int:
    #     """
    #     You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
    #     zero, and has a frequency greater than or equal to the value of the integer itself. 
    #     The frequency of an integer is the number of times it appears in the list.
    #     If no such a value exist, return -1.
    #     Examples:
    #     >>> search([4, 1, 2, 2, 3, 1])
    #     2
    #     >>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
    #     3
    #     >>> search([5, 5, 4, 4, 4])
    #     -1
    #     """

    #     lst.sort()
    #     prev, count = 0, 0
    #     for i, n in enumerate(lst):
    #         if n > prev:
    #             prev, count = n, 1
    #         elif n == prev:
    #             count += 1
    #         if count >= n:
    #             return n
    #     return -1

    # 2nd solution
    def search(lst: List[int]) -> int:
        """
        You are given a non-empty list of positive integers. Return the greatest integer that is greater than 
        zero, and has a frequency greater than or equal to the value of the integer itself. 
        The frequency of an integer is the number of times it appears in the list.
        If no such a value exist, return -1.
        Examples:
        >>> search([4, 1, 2, 2, 3, 1])
        2
        >>> search([1, 2, 2, 3, 3, 3, 4, 4, 4])
        3
        >>> search([5, 5, 4, 4, 4])
        -1
        """

        # create a dictionary to keep the frequency of each number
        freq = {}
        for n in lst:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1

        # get the greatest number
        num = max(freq.keys())

        # if there is no number, return -1
        if num < 1:
            return -1

        # if the frequency of the greatest number is greater than or equal to itself, return it
        if freq[num] >= num:
            return num

        # otherwise, return -1
        return -1
