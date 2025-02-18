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
        return ''

    # Find the longest palindrome that is a postfix of supplied string.
    palindrome = string[::-1]
    i = 0
    while i < len(string) and string[i] == palindrome[-i - 1]:
        i += 1
    postfix = string[-i:]

    # Find the longest prefix of the string that is a palindrome.
    prefix = ''
    i = 0
    while i < len(string) and string[i] == string[-i - 1]:
        i += 1
    prefix = string[:i]

    # Append to the end of the string a reverse of a string prefix that comes before the palindromic suffix.
    return prefix + postfix[::-1]
