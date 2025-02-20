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

    # Find the longest postfix of a string that is a palindrome.
    postfix_start_index = len(string) - 1
    while postfix_start_index > 0 and string[:postfix_start_index] != string[postfix_start_index::-1]:
        postfix_start_index -= 1
    # Return a string with a palindrome postfix and a reversed prefix that comes before the palindromic suffix.
    return string + string[postfix_start_index::-1]
