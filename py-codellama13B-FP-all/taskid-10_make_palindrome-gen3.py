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

    string_length = len(string)
    if string_length <= 1:
        return string

    # Find the longest suffix that is a palindrome
    palindrome_length = 1
    while palindrome_length < string_length:
        suffix = string[palindrome_length:]
        if suffix == suffix[::-1]:
            break
        palindrome_length += 1

    if palindrome_length == string_length:
        return string

    # Find the longest prefix that is a palindrome
    palindrome_length = 1
    while palindrome_length < string_length - palindrome_length:
        prefix = string[:string_length - palindrome_length]
        if prefix == prefix[::-1]:
            break
        palindrome_length += 1

    return f"{string}{string[::-1][palindrome_length:]}"
