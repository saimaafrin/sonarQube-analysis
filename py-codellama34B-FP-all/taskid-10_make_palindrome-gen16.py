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


    def is_palindrome(string):
        return string == string[::-1]

    if len(string) == 0:
        return ''

    suffix = string
    while len(suffix) > 0 and not is_palindrome(suffix):
        suffix = suffix[:-1]

    prefix = string[len(suffix) :]
    return string + prefix[::-1]
