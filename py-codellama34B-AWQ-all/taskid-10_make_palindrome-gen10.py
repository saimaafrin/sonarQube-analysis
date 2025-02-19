def make_palindrome(string: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    >>> make_palindrome('')
    ''
    >>> make_palindrome('cat')
    'catac'
    >>> make_palindrome('cata')
    'catac'
    """


    def is_palindrome(string: str) -> bool:
        """Check whether a string is palindrome.
        >>> is_palindrome('cat')
        False
        >>> is_palindrome('cata')
        True
        >>> is_palindrome('catac')
        True
        >>> is_palindrome('catacab')
        True
        """
        return string == string[::-1]

    if is_palindrome(string):
        return string

    # if the string is empty or consists of a single character
    # it can't be turned into palindrome
    if len(string) < 2:
        return ''

    # find the longest suffix that is palindrome
    # by iterating through the string backwards
    start = 0
    end = len(string)
    while not is_palindrome(string[start:end]):
        start += 1
        if start >= end - 1:
            return ''
    suffix = string[start:]

    # find the prefix of the string that comes before the suffix
    # and is not empty
    prefix = string[:start][::-1]
    if prefix == '':
        return ''

    # append the reverse of the prefix to the suffix
    return suffix + prefix
