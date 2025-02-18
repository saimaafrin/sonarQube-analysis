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
    if length == 0:
        return ''

    postfix = ''
    while length > 0:
        postfix = string[-length:]
        if postfix == postfix[::-1]:
            break
        length -= 1

    if length == 0:
        return string

    prefix = string[:length]

    return string + postfix[::-1]
