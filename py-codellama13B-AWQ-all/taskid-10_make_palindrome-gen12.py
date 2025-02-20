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

    # reverse the string
    rev = string[::-1]

    # find the longest postfix that is a palindrome
    postfix = ''
    for i in range(1, len(string) + 1):
        if string[-i:] == rev[:i]:
            postfix = string[-i:]

    # append to the end of the string the reverse of a string prefix that comes before the palindromic suffix
    return string + rev[:len(string) - len(postfix)]
