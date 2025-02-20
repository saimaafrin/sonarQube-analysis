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

    # Use the > comparison operator to determine which value is larger.
    # If the result is True, the first value is larger, and you should return the second value.
    # If the result is False, the second value is larger, and you should return the first value.
    # If both values are equal, return None.
    #
    # The operator you want to use is:
    # https://docs.python.org/3/reference/expressions.html#not-in
    if a > b:
        return b
    elif a < b:
        return a
    else:
        return None
