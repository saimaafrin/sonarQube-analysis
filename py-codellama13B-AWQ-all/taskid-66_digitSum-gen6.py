def digitSum(s: str) -> int:
    """Task
    Write a function that takes a string as input and returns the sum of the upper characters only'
    ASCII codes.

    Examples:
    >>> digitSum('')
    0
    >>> digitSum('abAB')
    131
    >>> digitSum('abcCd')
    67
    >>> digitSum('helloE')
    69
    >>> digitSum('woArBld')
    131
    >>> digitSum('aAaaaXa')
    153
    """

    return sum(ord(x.upper()) for x in s)
