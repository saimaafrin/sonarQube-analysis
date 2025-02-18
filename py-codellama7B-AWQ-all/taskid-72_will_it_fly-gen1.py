from typing import List

def will_it_fly(q: List[int], w: int) -> bool:
    """
    Write a function that returns True if the object q will fly, and False otherwise.
    The object q will fly if it's balanced (it is a palindromic list) and the sum of its elements is less than or equal the maximum possible weight w.

    Example:
    >>> will_it_fly([1, 2], 5)
    False
    # 1+2 is less than the maximum possible weight, but it's unbalanced.

    >>> will_it_fly([3, 2, 3], 1)
    False
    # it's balanced, but 3+2+3 is more than the maximum possible weight.

    >>> will_it_fly([3, 2, 3], 9)
    True
    # 3+2+3 is less than the maximum possible weight, and it's balanced.

    >>> will_it_fly([3], 5)
    True
    # 3 is less than the maximum possible weight, and it's balanced.
    """

    """
    We'll use 2 methods:
    - isBalanced to check if the list is balanced (it's a palindromic list).
    - sumElems to calculate the sum of all the elements in the list.
    """
    def isBalanced(q: List[int]) -> bool:
        """
        Check if the list is balanced (it's a palindromic list).
        Example:
        >>> isBalanced([1, 2, 1])
        True

        >>> isBalanced([1, 2, 3, 2, 1])
        True

        >>> isBalanced([1, 2, 3, 4, 5])
        False
        """
        """
        We'll use the 2-pointer method.
        If the sum of the left elements is equal to the sum of the right elements, then it's balanced.
        If not, then it's not balanced.
        """
        leftSum = 0
        rightSum = 0
        left = 0
        right = len(q) - 1
        while left < right:
            leftSum += q[left]
            rightSum += q[right]
            left += 1
            right -= 1
        if leftSum == rightSum:
            return True
        else:
            return False

    def sumElems(q: List[int]) -> int:
        """
        Calculate the sum of all the elements in the list.
        Example:
        >>> sumElems([1, 2, 3])
        6

        >>> sumElems([1, 2, 3, 4, 5])
        15
        """
        """
        We'll use the sum method.
        The sum of all the elements in the list is simply the sum of all the elements.
        """
        return sum(q)

    return isBalanced(q) and sumElems(q) <= w
