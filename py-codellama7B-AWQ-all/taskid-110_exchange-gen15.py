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

    if lst1 and lst2:
        if (len(lst1) == 0 and len(lst2) == 0) or (len(lst1) != 0 and len(lst2) != 0):
            for i in range(len(lst1)):
                for j in range(len(lst2)):
                    if (lst1[i] + lst2[j]) % 2 == 0:
                        if i == 0 and j == 0:
                            if lst1[i] % 2 == 0 and lst2[j] % 2 == 0:
                                return "YES"
                            elif lst1[i] % 2 == 0 and lst2[j] % 2 != 0:
                                lst2[j], lst1[i] = lst1[i], lst2[j]
                                return exchange(lst1, lst2)
                            elif lst1[i] % 2 != 0 and lst2[j] % 2 == 0:
                                lst1[i], lst2[j] = lst2[j], lst1[i]
                                return exchange(lst1, lst2)
                            else:
                                return "NO"
                        elif i == 0 and j != 0:
                            if lst1[i] % 2 == 0 and lst2[j] % 2 != 0:
                                lst2[j], lst1[i] = lst1[i], lst2[j]
                                return exchange(lst1, lst2)
                            elif lst1[i] % 2 != 0 and lst2[j] % 2 == 0:
                                lst1[i], lst2[j] = lst2[j], lst1[i]
                                return exchange(lst1, lst2)
                            else:
                                return "NO"
                        elif i != 0 and j == 0:
                            if lst1[i] % 2 == 0 and lst2[j] % 2 != 0:
                                lst1[i], lst2[j] = lst2[j], lst1[i]
                                return exchange(lst1, lst2)
                            elif lst1[i] % 2 != 0 and lst2[j] % 2 == 0:
                                lst2[j], lst1[i] = lst1[i], lst2[j]
                                return exchange(lst1, lst2)
                            else:
                                return "NO"
                        elif i != 0 and j != 0:
                            if lst1[i] % 2 == 0 and lst2[j] % 2 != 0:
                                lst1[i], lst2[j] = lst2[j], lst1[i]
                                return exchange(lst1, lst2)
                            elif lst1[i] % 2 != 0 and lst2[j] % 2 == 0:
                                lst2[j], lst1[i] = lst1[i], lst2[j]
                                return exchange(lst1, lst2)
                            else:
                                return "NO"
                    else:
                        continue
    return "NO"
