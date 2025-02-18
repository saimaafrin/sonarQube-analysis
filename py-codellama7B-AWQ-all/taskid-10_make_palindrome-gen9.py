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

    result = string
    if not is_palindrome(string):
        palindromic_suffix = find_longest_palindromic_suffix(string)
        string_prefix = string[:-len(palindromic_suffix)]
        result = string_prefix + palindromic_suffix + reverse(palindromic_suffix)
    return result
