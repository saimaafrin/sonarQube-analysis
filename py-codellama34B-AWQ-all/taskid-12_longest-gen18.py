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

    if strings == []:
        return None
    max = 0
    max_index = 0
    for i in range(len(strings)):
        if len(strings[i]) > max:
            max = len(strings[i])
            max_index = i
    return strings[max_index]
