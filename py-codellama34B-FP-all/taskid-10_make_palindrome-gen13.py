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

    # if string is already a palindrome, just return it
    if string == string[::-1]:
        return string

    # find the longest postfix of the string that is palindrome
    postfix_len = 1
    while not string[-postfix_len:] == string[-postfix_len:][::-1]:
        postfix_len += 1

    return string + string[:postfix_len][::-1]
