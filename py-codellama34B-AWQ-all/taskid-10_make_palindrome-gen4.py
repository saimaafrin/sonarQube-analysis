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
    for i in range(len(string)):
        palindrome = string[i:]
        if palindrome == palindrome[::-1]:
            break
    return string + string[:len(string)-len(palindrome)][::-1]
