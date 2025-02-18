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

    # Find the longest postfix of supplied string that is a palindrome.
    # If there is no postfix then the entire string is a palindrome.
    palindrome_postfix = string
    while not palindrome_postfix[::-1].startswith(palindrome_postfix):
        palindrome_postfix = palindrome_postfix[:-1]
    # Find the longest prefix that comes before the palindromic suffix.
    palindrome_prefix = string[:-len(palindrome_postfix)]
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    return f"{string}{palindrome_prefix[::-1]}"
