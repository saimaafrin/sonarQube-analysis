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
    if string == string[::-1]:
        return string
    postfix_is_palindrome = False
    for i in range(1, len(string)):
        if string[-i:] == string[-i:][::-1]:
            postfix_is_palindrome = True
            break
    if not postfix_is_palindrome:
        return string
    postfix_length = i
    postfix_start = -i
    prefix_start = -i - 1
    prefix_is_palindrome = True
    for i in range(1, postfix_length):
        if string[prefix_start:-i] != string[prefix_start:-i][::-1]:
            prefix_is_palindrome = False
            break
    if prefix_is_palindrome:
        return string
    prefix_length = i
    return string[:-prefix_length] + string[prefix_start:postfix_start][::-1]
