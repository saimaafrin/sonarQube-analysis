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

    # Find the longest postfix of supplied string that is a palindrome
    palindromic_suffix = find_palindromic_suffix(string)

    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix
    prefix = string[:string.find(palindromic_suffix)]
    return string + prefix[::-1]
