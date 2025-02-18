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

    # TODO: Implement this function
    if a == b:
        return None
    elif type(a) == int and type(b) == int:
        if a > b:
            return a
        else:
            return b
    elif type(a) == float and type(b) == float:
        if a > b:
            return a
        else:
            return b
    elif type(a) == str and type(b) == str:
        a_f = a.replace(',', '.')
        b_f = b.replace(',', '.')
        if float(a_f) > float(b_f):
            return a_f
        else:
            return b_f
    elif type(a) == int and type(b) == str:
        if a > float(b.replace(',', '.')):
            return a
        else:
            return b.replace(',', '.')
    elif type(a) == str and type(b) == int:
        if float(a.replace(',', '.')) > b:
            return a.replace(',', '.')
        else:
            return b
    elif type(a) == float and type(b) == str:
        if a > float(b.replace(',', '.')):
            return a
        else:
            return b.replace(',', '.')
    elif type(a) == str and type(b) == float:
        if float(a.replace(',', '.')) > b:
            return a.replace(',', '.')
        else:
            return b
