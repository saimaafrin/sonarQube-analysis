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

    length = len(string)
    if length <= 1:
        return string
    for i in range(length - 1, 0, -1):
        if string[0:i] == string[0:i][::-1]:
            return string + string[0:i][::-1]
    return string
