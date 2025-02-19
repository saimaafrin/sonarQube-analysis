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

    def cast_type(num: Union[int, float, str]) -> float:
        if isinstance(num, str):
            if ',' in num:
                num = float(num.replace(',', '.'))
            else:
                num = float(num)
        return num

    a = cast_type(a)
    b = cast_type(b)

    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b
