from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    if len(string) == 0:
        return []
    else:
        return [string[0:i+1] for i in range(len(string))]
