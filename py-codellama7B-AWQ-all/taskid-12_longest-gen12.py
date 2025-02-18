from typing import List, Optional

def longest(strings: List[str]) -> Optional[str]:
    """ Out of list of strings, return the longest one. Return the first one in case of multiple
    strings of the same length. Return None in case the input list is empty.
    >>> longest([])
    None
    >>> longest(['a', 'b', 'c'])
    'a'
    >>> longest(['a', 'bb', 'ccc'])
    'ccc'
    """

    if len(strings) == 0:
        return None
    longest_string = None
    longest_string_length = -1
    for string in strings:
        if len(string) > longest_string_length:
            longest_string = string
            longest_string_length = len(string)
    return longest_string
