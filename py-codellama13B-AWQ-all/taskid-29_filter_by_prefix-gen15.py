from typing import List

def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """


    # TODO: Write a loop that goes through all strings in the list and
    # filters out all the strings that do not start with the given prefix.
    result = []
    for s in strings:
        if s.startswith(prefix):
            result.append(s)

    return result
