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

    # replace the string with all uppercase letters
    # then split into a list
    # create an empty list to store the ascii numbers
    # use a for loop to iterate through the list, and append the ASCII number to the empty list
    # use the sum function to add the elements of the list
    return sum([ord(s.upper()) for s in str.split()])
