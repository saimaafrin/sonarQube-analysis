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
    reverse = string[::-1]
    prefix_len = len(string) - (len(string) - reverse.find(reverse))
    suffix_len = len(reverse) - (len(reverse) - reverse.find(reverse))
    return string + reverse[:prefix_len]
