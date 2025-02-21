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
    longest_string = strings[0]
    for s in strings[1:]:
        if len(s) > len(longest_string):
            longest_string = s
        elif len(s) == len(longest_string):
            longest_string = strings[0]
    return longest_string
