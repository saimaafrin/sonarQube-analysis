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

    if string == '':
        return string

    # Reverse the string.
    rev_string = string[::-1]

    # Find the longest postfix of the string that is a palindrome.
    # This is the suffix of the string.
    suffix = rev_string
    for i in range(len(rev_string) - 1, 0, -1):
        if rev_string[0:i] == rev_string[0:i][::-1]:
            suffix = rev_string[0:i]
            break

    # Find the prefix of the string.
    prefix = string[0:len(string) - len(suffix)]

    # Find the longest prefix of the string that is a palindrome.
    # This is the prefix of the string.
    prefix_rev = prefix[::-1]
    for i in range(len(prefix_rev) - 1, 0, -1):
        if prefix_rev == prefix_rev[0:i][::-1]:
            prefix = prefix[0:i]
            break

    return prefix + rev_string + prefix[::-1]
