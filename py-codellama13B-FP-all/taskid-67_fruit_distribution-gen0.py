def fruit_distribution(s: str, n: int) -> int:
    """
    In this task, you will be given a string that represents a number of apples and oranges 
    that are distributed in a basket of fruit this basket contains 
    apples, oranges, and mango fruits. Given the string that represents the total number of 
    the oranges and apples and an integer that represent the total number of the fruits 
    in the basket return the number of the mango fruits in the basket.
    for examble:
    >>> fruit_distribution('5 apples and 6 oranges', 19)
    8
    >>> fruit_distribution('0 apples and 1 oranges', 3)
    2
    >>> fruit_distribution('2 apples and 3 oranges', 100)
    95
    >>> fruit_distribution('100 apples and 1 oranges', 120)
    19
    """

    result = n
    apples = s.split(" ")[0]
    oranges = s.split(" ")[3]
    result -= (int(apples) + int(oranges))
    return result
