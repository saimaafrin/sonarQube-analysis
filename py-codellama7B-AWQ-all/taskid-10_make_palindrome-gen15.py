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

    rev = string[::-1]
    palindromic_suffix_start = len(string) - len(string.lstrip(rev))
    palindromic_suffix = string[palindromic_suffix_start:]

    if palindromic_suffix == string:
        return string

    prefix_start = len(string) - palindromic_suffix_start
    prefix = string[:prefix_start]
    suffix = palindromic_suffix[len(palindromic_suffix) // 2:]

    return string + suffix[::-1] + prefix
