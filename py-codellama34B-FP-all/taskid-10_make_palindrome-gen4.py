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

    i = 0
    j = 1

    while j < len(string):
        if string[i] != string[j]:
            i = 0
        else:
            i += 1
            j += 1

    return string + string[i:len(string)-1-i][::-1]
