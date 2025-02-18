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

    longest_palindrome = string + string[::-1]
    prefix = ''
    suffix = ''
    for i in range(len(longest_palindrome)):
        if longest_palindrome[i:].startswith(string):
            suffix = longest_palindrome[i:]
            prefix = longest_palindrome[:i]
            break
    return prefix + suffix[::-1]
