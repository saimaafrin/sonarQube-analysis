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
    i = length // 2
    while i < length:
        left_slice = string[:i]
        right_slice = string[i:]
        if right_slice == left_slice[::-1]:
            return string + left_slice[::-1]
        i += 1
    return string
