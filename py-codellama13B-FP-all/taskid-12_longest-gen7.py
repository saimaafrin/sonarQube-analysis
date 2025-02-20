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
    max_len = len(strings[0])
    max_strings = strings[0:1]
    for s in strings[1:]:
        if len(s) > max_len:
            max_len = len(s)
            max_strings = [s]
        elif len(s) == max_len:
            max_strings.append(s)
    return max_strings[0]
