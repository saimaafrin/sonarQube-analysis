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

    string_len = len(string)
    if string_len < 2:
        return string

    # 2. Find the longest postfix of supplied string that is a palindrome.
    # Algorithm is O(n)
    postfix_len = 1  # we start with postfix length 1
    while postfix_len < string_len:
        if string[postfix_len:] == string[:-postfix_len][::-1]:
            postfix_len += 1
        else:
            break

    # 1. Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    # Algorithm is O(n)
    return string[:-postfix_len] + string[postfix_len:][::-1]
