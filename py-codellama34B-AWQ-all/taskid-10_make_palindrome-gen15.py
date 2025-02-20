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

    if string == string[::-1]:
        return string

    # find longest postfix of input string that is a palindrome
    max_len = len(string)
    for i in range(max_len, 0, -1):
        if string[-i:] == string[-i:][::-1]:
            max_len = i
            break

    return string + string[:max_len-1][::-1]
