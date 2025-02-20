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

    if type(a) is int and type(b) is int:
        return max(a, b)
    elif type(a) is float and type(b) is float:
        return max(a, b)
    elif type(a) is str and type(b) is str:
        a_float = float(a.replace(',', '.'))
        b_float = float(b.replace(',', '.'))
        if a_float > b_float:
            return a
        elif a_float < b_float:
            return b
        else:
            return None
    else:
        raise TypeError(f'Compare_one() requires that both parameters are of the same type. {a} is not {type(a)}')
