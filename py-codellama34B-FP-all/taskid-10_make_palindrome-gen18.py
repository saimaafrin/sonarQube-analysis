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

    # find the middle of the string
    i, j = 0, len(string) - 1
    while i < j:
        if string[i] != string[j]:
            break
        i += 1
        j -= 1

    # reverse the first half of the string
    # and return the concatenation of the string and the reversed prefix
    return string + string[i:j+1][::-1]
