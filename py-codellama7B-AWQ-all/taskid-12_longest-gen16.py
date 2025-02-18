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
    longest = strings[0]
    for i in range(1, len(strings)):
        if len(strings[i]) > len(longest):
            longest = strings[i]
    return longest
