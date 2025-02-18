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

    # First, find the longest postfix of supplied string that is a palindrome:
    n = len(string)
    # Reverse the string and find the first position
    # where the first characters of the reversed string and original string are not equal:
    i = 0
    while i < n // 2 and string[i] == string[n - i - 1]:
        i += 1

    # Find the first position where the first character of the original string is different from the
    # first character of the reversed string:
    prefix = string[:n - i]
    suffix = string[i:]

    # Find the longest prefix of the suffix that is a palindrome:
    n = len(suffix)
    i = 0
    while i < n // 2 and suffix[i] == suffix[n - i - 1]:
        i += 1

    # Make a palindrome from the prefix by concatenating the prefix with the reversed suffix:
    return prefix + suffix[i:][::-1]
