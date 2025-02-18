from typing import Union

def compare_one(a: Union[int, float, str], b: Union[int, float, str]) -> Union[int, float, str, None]:
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    >>> compare_one(1, 2.5)
    2.5
    >>> compare_one(1, '2,3')
    '2,3'
    >>> compare_one('5,1', '6')
    '6'
    >>> compare_one('1', 1)
    None
    """

    # Your code here
    if a == b:
        return None
    if isinstance(a, str):
        if isinstance(b, int):
            return a
        elif isinstance(b, str):
            if a[0] == ',':
                return b
            elif b[0] == ',':
                return a
            elif float(a) > float(b):
                return a
            else:
                return b
        else:
            return a
    elif isinstance(a, int):
        if isinstance(b, int):
            return a if a > b else b
        elif isinstance(b, str):
            return b
        else:
            return a
    else:
        if isinstance(b, int):
            return b
        elif isinstance(b, str):
            return a
        else:
            return a
