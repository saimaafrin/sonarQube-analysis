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

    if isinstance(a, str) or isinstance(b, str):
        a_str = str(a)
        b_str = str(b)
        if a_str == b_str:
            return None
        else:
            return a_str if a_str > b_str else b_str
    else:
        return b if a < b else a
