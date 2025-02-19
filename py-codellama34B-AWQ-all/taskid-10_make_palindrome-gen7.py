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

    string = string.lower()
    n = len(string)
    i, j = 0, n - 1
    while i <= j:
        if string[i] == string[j]:
            i += 1
            j -= 1
        else:
            j -= 1
    first_half = string[i:]
    return string + first_half[::-1]
