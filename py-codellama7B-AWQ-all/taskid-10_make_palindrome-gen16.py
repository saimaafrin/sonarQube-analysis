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

    max_prefix = find_longest_prefix_palindrome(string)
    min_suffix = find_shortest_suffix_palindrome(string)
    if max_prefix == min_suffix:
        return string

    result = string[:len(string) - len(min_suffix)] + min_suffix
    return result
