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

    palindrome = string
    # Reverse string.
    rev = string[::-1]
    # Find a longest postfix that is a palindrome.
    postfix = ''
    for i in range(len(string)):
        if palindrome[i:] == rev[i:]:
            postfix = palindrome[i:]
    # Append the reverse of the prefix to the end of the string.
    if postfix:
        prefix = string[:-len(postfix)]
        return prefix + rev[:len(postfix)]
    return palindrome
