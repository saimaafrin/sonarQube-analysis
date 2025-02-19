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


    def is_upper_char(char: str) -> bool:
        return char.isupper()

    def to_ascii_code(char: str) -> int:
        return ord(char)

    def is_digit(char: str) -> bool:
        return char.isdigit()

    return sum(map(to_ascii_code, filter(is_upper_char, filter(is_digit, s))))
