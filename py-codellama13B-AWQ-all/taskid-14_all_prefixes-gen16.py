from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    # TODO: write the code to generate all prefixes of a string
    result = []
    for i in range(len(string)+1):
        result.append(string[:i])
    return result
