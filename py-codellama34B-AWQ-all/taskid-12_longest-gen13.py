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

    # your code here
    if not strings:
        return None
    max_len = 0
    max_str = ""
    for s in strings:
        if len(s) > max_len:
            max_len = len(s)
            max_str = s
    return max_str
