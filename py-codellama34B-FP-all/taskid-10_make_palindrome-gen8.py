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
    for suffix_len in range(len(string), 0, -1):
        suffix = string[-suffix_len:]
        if suffix == suffix[::-1]:
            prefix = string[:-suffix_len]
            return string + prefix[::-1]
    raise ValueError('Failed to make a palindrome')
