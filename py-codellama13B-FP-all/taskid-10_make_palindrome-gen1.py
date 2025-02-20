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

    length = len(string)
    if length == 0:
        return ''

    left = 0
    right = length - 1

    while left < right and string[left] == string[right]:
        left += 1
        right -= 1

    if left == right:
        return string + string[left]

    postfix = string[right:]
    if is_palindrome(postfix):
        return string + reverse_string(postfix)

    return string + reverse_string(postfix) + postfix
