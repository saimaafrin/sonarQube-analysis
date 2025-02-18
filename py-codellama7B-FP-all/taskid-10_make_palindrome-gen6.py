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

    if not string or len(string) == 1:
        return string
    palindromic_suffix = ''
    for i in range(len(string)):
        if string[i:] == string[i:][::-1]:
            palindromic_suffix = string[i:]
    # Get the reverse of the prefix that comes before the palindromic suffix.
    prefix_reverse = string[:len(string) - len(palindromic_suffix)]
    return string + prefix_reverse[::-1]
