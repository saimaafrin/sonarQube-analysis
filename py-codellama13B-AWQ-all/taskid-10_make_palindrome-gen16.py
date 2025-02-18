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

    if len(string) == 0:
        return ''

    # 1. Find the longest postfix of supplied string that is a palindrome.
    postfix_idx = len(string) - 1
    while postfix_idx > 0 and string[postfix_idx] == string[0]:
        postfix_idx -= 1

    # 2. Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    prefix = string[:postfix_idx + 1]
    return prefix + prefix[::-1]
