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

    if not string:
        return ''
    suffix = ''
    for i in range(len(string)):
        prefix = string[:i + 1]
        if prefix == prefix[::-1]:
            suffix = string[i + 1:]
            break
    return f'{string}{suffix[::-1]}'
