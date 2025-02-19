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
        return string

    longest_palindrome_prefix_length = 0

    for i in range(len(string)):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            longest_palindrome_prefix_length = i

    prefix = string[:longest_palindrome_prefix_length + 1]
    return prefix + prefix[::-1]
