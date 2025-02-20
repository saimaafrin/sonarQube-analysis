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


    prefix_palindrome = ''
    for i in range(len(string) - 1, -1, -1):
        sub_string = string[i:]
        if sub_string == sub_string[::-1]:
            prefix_palindrome = sub_string
            break

    suffix_palindrome = ''
    for i in range(len(string)):
        sub_string = string[:i + 1]
        if sub_string == sub_string[::-1]:
            suffix_palindrome = sub_string
            break

    return prefix_palindrome + suffix_palindrome[::-1]
