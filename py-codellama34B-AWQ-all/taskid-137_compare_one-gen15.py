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


    def _compare(a, b):
        return a if a > b else b if b > a else None

    def _real_to_float(s):
        s = s.replace(',', '.')
        return float(s)

    if isinstance(a, (float, int)):
        if isinstance(b, (float, int)):
            return _compare(a, b)
        elif isinstance(b, str):
            return _compare(a, _real_to_float(b))
    elif isinstance(a, str):
        if isinstance(b, (float, int)):
            return _compare(_real_to_float(a), b)
        elif isinstance(b, str):
            return _compare(_real_to_float(a), _real_to_float(b))
    return None
