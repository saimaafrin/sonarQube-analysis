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

    if string == '':
        return ''
    suffix = ''
    i = 0
    while i < len(string) and string[i] == string[~i]:
        suffix = string[i] + suffix
        i += 1
    return string + suffix[::-1]
