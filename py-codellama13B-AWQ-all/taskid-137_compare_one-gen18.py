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

    if type(a) == type(b):
        if a > b:
            return a
        elif b > a:
            return b
        else:
            return None
    elif type(a) == str and type(b) == float:
        return compare_one(float(a), b)
    elif type(a) == float and type(b) == str:
        return compare_one(a, float(b))
    elif type(a) == int and type(b) == str:
        return compare_one(a, float(b))
    elif type(a) == str and type(b) == int:
        return compare_one(float(a), b)
