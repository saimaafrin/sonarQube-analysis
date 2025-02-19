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

    if a == b:
        return None

    # 1.
    # if isinstance(a, str) and isinstance(b, str):
    #     return a if float(a.replace(',', '.')) < float(b.replace(',', '.')) else b
    #
    # if isinstance(a, str) and isinstance(b, (int, float)):
    #     return b if float(a.replace(',', '.')) < b else a
    #
    # if isinstance(b, str) and isinstance(a, (int, float)):
    #     return a if a < float(b.replace(',', '.')) else b

    if isinstance(a, str):
        a = float(a.replace(',', '.'))
    if isinstance(b, str):
        b = float(b.replace(',', '.'))

    return a if a < b else b
