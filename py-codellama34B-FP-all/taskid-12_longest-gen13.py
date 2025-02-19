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

    # The following line will throw an exception if the input is not a list of strings.
    # We do not catch this exception.
    strings[0].upper()

    if len(strings) == 0:
        return None

    current_longest = strings[0]
    for string in strings:
        if len(string) > len(current_longest):
            current_longest = string
    return current_longest
