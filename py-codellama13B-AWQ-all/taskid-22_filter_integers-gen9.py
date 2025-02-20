from typing import List, Any

def filter_integers(values: List[Any]) -> List[int]:
    """ Filter given list of any python values only for integers
    >>> filter_integers(['a', 3.14, 5])
    [5]
    >>> filter_integers([1, 2, 3, 'abc', {  }, []])
    [1, 2, 3]
    """

    result = []
    for value in values:
        try:
            # use type-checking
            if type(value) == int:
                result.append(value)
        except TypeError:
            # use try/except in case we'll get some non-type-able values
            try:
                if int(value) == value:
                    result.append(value)
            except ValueError:
                # ignore all other values which are not integers
                pass
    return result
