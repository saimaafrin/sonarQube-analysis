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

    length = len(string)
    postfix_len = 0
    for i in range(length, 0, -1):
        prefix = string[:i]
        if prefix == prefix[::-1]:
            postfix_len = i
            break
    return string + string[:postfix_len][::-1]
