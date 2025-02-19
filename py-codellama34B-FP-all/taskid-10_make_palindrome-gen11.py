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

    suffix_start_index = 0
    for i in range(len(string) - 1, -1, -1):
        if string[i] == string[len(string) - 1 - i + suffix_start_index]:
            suffix_start_index += 1
        else:
            break
    return string + string[len(string) - suffix_start_index:len(string) - suffix_start_index - 1:-1]
