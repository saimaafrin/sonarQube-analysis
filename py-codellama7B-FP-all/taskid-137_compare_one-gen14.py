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

    if isinstance(a, str) and isinstance(b, str):
        return a if a > b else b
    if isinstance(a, int) and isinstance(b, float):
        return a if a > b else b
    if isinstance(a, float) and isinstance(b, int):
        return a if a > b else b
    return None
