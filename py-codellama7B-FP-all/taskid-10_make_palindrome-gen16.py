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

    def is_palindrome(string: str) -> bool:
        return string == string[::-1]

    longest_palindrome = ''
    for i in range(len(string), 0, -1):
        if is_palindrome(string[:i]):
            longest_palindrome = string[:i]
            break
    return string + longest_palindrome[::-1]
