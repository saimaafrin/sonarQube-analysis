from typing import List

def all_prefixes(string: str) -> List[str]:
    """ Return list of all prefixes from shortest to longest of the input string
    >>> all_prefixes('abc')
    ['a', 'ab', 'abc']
    """

    # initialize the output prefix list
    prefixes = []
    # loop through the indices of the string
    for i in range(len(string)):
        # append the prefix from position 0 to the current position to the list of prefixes
        prefixes.append(string[:i+1])
    # return the list of prefixes
    return prefixes
