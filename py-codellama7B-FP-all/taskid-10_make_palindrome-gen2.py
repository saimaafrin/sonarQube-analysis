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

    def reverse(s: str) -> str:
        return s[::-1]

    def is_palindrome(s: str) -> bool:
        return s == reverse(s)

    def longest_postfix(s: str) -> str:
        i = len(s) - 1
        while i >= 0 and is_palindrome(s[:i + 1]):
            i -= 1
        return s[i + 1:]

    def shortest_prefix(s: str) -> str:
        i = 0
        while i < len(s) and is_palindrome(s[i:]):
            i += 1
        return s[:i]

    return string + reverse(shortest_prefix(longest_postfix(string)))
