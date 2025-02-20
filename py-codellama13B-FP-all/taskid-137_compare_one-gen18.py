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

    # if a and b are both numbers
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return max(a, b)
    # if both a and b are strings
    elif isinstance(a, str) and isinstance(b, str):
        return max(a, b)
    # if only one is a string
    elif isinstance(a, str):
        return b
    # if only one is a number
    elif isinstance(b, str):
        return a
    # if a and b are both numbers but different types
    elif isinstance(a, float) and isinstance(b, int):
        return a
    # if a and b are both numbers but different types
    elif isinstance(a, int) and isinstance(b, float):
        return b
    # if one is a float and one is an int
    elif isinstance(a, float) and isinstance(b, int):
        return a
    # if one is an int and one is a float
    elif isinstance(a, int) and isinstance(b, float):
        return b
    # if they are equal
    else:
        return None
