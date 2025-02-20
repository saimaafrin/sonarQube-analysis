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

    def clean_number(value: Union[int, float, str]) -> float:
        if isinstance(value, str):
            return float(value.replace(',', '.'))
        return float(value)

    a_float = clean_number(a)
    b_float = clean_number(b)
    if a_float == b_float:
        return None
    return a if a_float > b_float else b
