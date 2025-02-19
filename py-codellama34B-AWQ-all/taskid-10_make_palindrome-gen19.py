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
    length = len(string)
    is_palindrome = [False] * length
    is_palindrome[-1] = True
    for i in range(length - 2, -1, -1):
        is_palindrome[i] = string[i] == string[i + 1] and is_palindrome[i + 1]
    longest_palindromic_suffix_length = 0
    for i in range(length):
        if is_palindrome[i]:
            longest_palindromic_suffix_length = i + 1
    return string + string[longest_palindromic_suffix_length::-1]
