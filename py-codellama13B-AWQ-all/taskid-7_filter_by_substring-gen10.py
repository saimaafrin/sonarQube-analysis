from typing import List

def filter_by_substring(strings: List[str], substring: str) -> List[str]:
    """ Filter an input list of strings only for ones that contain given substring
    >>> filter_by_substring([], 'a')
    []
    >>> filter_by_substring(['abc', 'bacd', 'cde', 'array'], 'a')
    ['abc', 'bacd', 'array']
    """

    # filter is a builtin function in Python that is designed to work with iterables.
    # In this case the iterable is a list, but it could be any type that is iterable
    # (like a tuple or dictionary).
    #
    # The callable object to use to filter the elements of the iterable is passed as
    # the first argument to the filter() function. It will be called with the
    # elements from the iterable and should return True or False if the element
    # should be kept in the output.
    return list(filter(lambda s: substring in s, strings))
