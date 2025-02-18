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


    def find_longest_postfix(s, suffix):
        start = len(s) - 1
        for i in range(len(suffix) - 1, -1, -1):
            if s[start] == suffix[i]:
                start -= 1
            else:
                break
        return s[start + 1:]

    suffix = find_longest_postfix(string, string)
    return string + suffix[::-1]
