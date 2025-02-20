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

    odd_len_lst = []
    for str_ in lst:
        if len(str_) % 2 != 0:
            odd_len_lst.append(str_)
    even_len_lst = list(set(lst) - set(odd_len_lst))
    return sorted(even_len_lst)
