def truncate_number(number: float) -> float:
    """ Given a positive floating point number, it can be decomposed into
    and integer part (largest integer smaller than given number) and decimals
    (leftover part always smaller than 1).

    Return the decimal part of the number.
    >>> truncate_number(3.5)
    0.5
    """

    assert isinstance(number, float)
    assert number > 0

    integer_part, decimals = str(number).split('.')

    assert len(decimals) == 1

    return float(decimals)
