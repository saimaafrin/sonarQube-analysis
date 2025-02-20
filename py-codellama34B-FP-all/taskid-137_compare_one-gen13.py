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

    def try_compare(a, b):
        return a if a > b else None

    def try_compare_str(a, b):
        return a if float(a.replace(',', '.')) > float(b.replace(',', '.')) else None

    if type(a) == type(b):
        return try_compare(a, b)
    elif type(a) == str and type(b) == float:
        return try_compare(float(a.replace(',', '.')), b)
    elif type(a) == float and type(b) == str:
        return try_compare(a, float(b.replace(',', '.')))
    elif type(a) == str and type(b) == int:
        return try_compare(float(a.replace(',', '.')), b)
    elif type(a) == int and type(b) == str:
        return try_compare(a, float(b.replace(',', '.')))
    elif type(a) == str and type(b) == str:
        return try_compare_str(a, b)

    return None
