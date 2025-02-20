from typing import List

def exchange(lst1: List[int], lst2: List[int]) -> str:
    """In this problem, you will implement a function that takes two lists of numbers,
    and determines whether it is possible to perform an exchange of elements
    between them to make lst1 a list of only even numbers.
    There is no limit on the number of exchanged elements between lst1 and lst2.
    If it is possible to exchange elements between the lst1 and lst2 to make
    all the elements of lst1 to be even, return "YES".
    Otherwise, return "NO".
    For example:
    >>> exchange([1, 2, 3, 4], [1, 2, 3, 4])
    'YES'
    >>> exchange([1, 2, 3, 4], [1, 5, 3, 4])
    'NO'
    It is assumed that the input lists will be non-empty.
    """

    # This problem can be solved using Breadth First Search (BFS).
    # You can use a queue to keep track of the next states.
    # In each state, you can either exchange one element from lst1 with
    # one element from lst2, or you can exchange two elements from lst1
    # with two elements from lst2.
    # You can also use a visited set to prevent visiting the same state
    # more than once.
    pass
