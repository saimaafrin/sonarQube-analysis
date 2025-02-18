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

    if string == '':
        return string
    prefix_length = 1
    for i in range(1, len(string)):
        if string[:i] == string[len(string) - i:]:
            prefix_length = i
            break
    return string + string[len(string) - prefix_length:][::-1]
