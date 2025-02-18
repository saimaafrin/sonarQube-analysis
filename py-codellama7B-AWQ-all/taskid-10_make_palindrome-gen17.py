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

    palindrome = ''
    for length in range(len(string), 0, -1):
        substr = string[:length]
        if substr == substr[::-1]:
            palindrome = substr
            break
    if len(palindrome) > 0:
        prefix = string[:len(string) - len(palindrome)]
        suffix = string[len(string) - len(palindrome):]
        return prefix + suffix[::-1] + palindrome
    else:
        return string + string[::-1]
