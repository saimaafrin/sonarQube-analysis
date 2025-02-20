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

    if not strings:
        return None
    strings = sorted(strings, key=len, reverse=True)
    first_len = len(strings[0])
    for i, s in enumerate(strings):
        if len(s) != first_len:
            return strings[i-1]
    return strings[0]
