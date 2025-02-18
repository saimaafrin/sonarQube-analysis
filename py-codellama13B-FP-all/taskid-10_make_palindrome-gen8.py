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

    if not string:
        return string
    reversed_string = string[::-1]
    longest_suffix = ''
    for i in range(len(string)):
        suffix = string[-(i + 1):]
        if suffix == reversed_string[:i + 1]:
            longest_suffix = suffix
        else:
            break
    return string + reversed_string[:len(longest_suffix)]
