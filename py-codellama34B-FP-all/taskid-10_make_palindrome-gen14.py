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

    # Find longest postfix of string that is also a prefix
    # We can find it in linear time with two pointers
    start = 0
    end = 1
    while end < len(string):
        if string[start] == string[end]:
            start += 1
            end += 1
        elif start > 0:
            start = 0
            end += 1
        else:
            end += 1

    # If the whole string is a palindrome, we are done
    if start == len(string):
        return string

    # Otherwise we need to append reverse of the prefix to the end of the string
    return string + string[end - 1::-1]
