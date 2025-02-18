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


    # A dictionary is used to keep track of the count of every element in the list
    lst1_dict = {}
    for element in lst1:
        if element in lst1_dict:
            lst1_dict[element] += 1
        else:
            lst1_dict[element] = 1

    # Iterate through lst2 to see if any element can be used to make
    # the elements of lst1 to be even
    for element in lst2:
        # If the current element of lst2 is even, continue
        if element % 2 == 0:
            continue
        # If the current element of lst2 is odd,
        # try to use it to make the elements of lst1 even
        else:
            # If the current element of lst2 can be used to make an
            # even element of lst1, increment the count of that element
            if element * 2 in lst1_dict:
                lst1_dict[element * 2] += 1
            # If the current element of lst2 cannot be used to make any
            # even element of lst1, return "NO"
            else:
                return "NO"

    # If all the elements of lst1 can be even by using elements of lst2, return "YES"
    return "YES"
