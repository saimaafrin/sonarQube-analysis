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

    # First, let's find a longest postfix of the supplied string that is a palindrome.
    postfix = ''
    for i in range(len(string), 0, -1):
        if string[-i:] == string[:i]:
            postfix = string[-i:]
            break

    if not postfix:
        return string

    prefix = string[:-len(postfix)]
    return prefix + postfix[::-1]
