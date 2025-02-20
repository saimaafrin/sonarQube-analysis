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

    if is_palindrome(string):
        return string

    longest_palindromic_suffix = longest_palindromic_suffix_of(string)
    suffix_length = len(longest_palindromic_suffix)
    palindromic_suffix_prefix = string[: -suffix_length]
    return string + reverse(palindromic_suffix_prefix)
