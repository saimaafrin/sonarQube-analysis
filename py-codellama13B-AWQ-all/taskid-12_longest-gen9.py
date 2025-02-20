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
    longest_string: Optional[str] = None
    longest_length = -1
    for s in strings:
        if len(s) > longest_length:
            longest_length = len(s)
            longest_string = s
    return longest_string
