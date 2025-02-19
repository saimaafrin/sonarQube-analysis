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

    max_str: Optional[str] = None
    max_len: int = 0

    for str in strings:
        len_str = len(str)
        if len_str > max_len:
            max_len = len_str
            max_str = str

    return max_str
