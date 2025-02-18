from typing import List

def sorted_list_sum(lst: List[str]) -> List[str]:
    """Write a function that accepts a list of strings as a parameter,
    deletes the strings that have odd lengths from it,
    and returns the resulted list with a sorted order,
    The list is always a list of strings and never an array of numbers,
    and it may contain duplicates.
    The order of the list should be ascending by length of each word, and you
    should return the list sorted by that rule.
    If two words have the same length, sort the list alphabetically.
    The function should return a list of strings in sorted order.
    You may assume that all words will have the same length.
    For example:
    >>> list_sort(['aa', 'a', 'aaa'])
    ['aa']
    >>> list_sort(['ab', 'a', 'aaa', 'cd'])
    ['ab', 'cd']
    """

    odd_length = []
    even_length = []
    for i in lst:
        if len(i) % 2 != 0:
            odd_length.append(i)
        else:
            even_length.append(i)
    sorted_even_length = sorted(even_length)
    sorted_odd_length = sorted(odd_length)
    return sorted_even_length + sorted_odd_length
