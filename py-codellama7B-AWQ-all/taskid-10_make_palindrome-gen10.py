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

    # Longest palindrome suffix
    palindrome_suffix = ''
    for i in range(len(string)):
        palindrome_suffix = string[i:]
        if palindrome_suffix == palindrome_suffix[::-1]:
            break

    # Longest palindrome prefix
    palindrome_prefix = ''
    for i in range(len(string)):
        palindrome_prefix = string[:-i]
        if palindrome_prefix == palindrome_prefix[::-1]:
            break

    return string + palindrome_prefix[::-1]
