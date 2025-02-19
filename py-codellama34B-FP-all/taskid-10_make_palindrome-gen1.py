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

    n = len(string)
    # Find the longest palindromic suffix of the string.
    # It is a part of a string that is the same as its reverse.
    # Palindromic suffix is always a suffix of the string.
    longest_palindromic_suffix = ''
    for i in range(n, -1, -1):
        suffix = string[i:]
        if suffix == suffix[::-1]:
            longest_palindromic_suffix = suffix
            break
    # Now we need to add to the end of the string
    # a reversed prefix of the string, that comes before
    # the palindromic suffix.
    # There is no such prefix if palindromic suffix
    # is the whole string.
    if longest_palindromic_suffix == string:
        return string
    prefix_length = n - len(longest_palindromic_suffix)
    return string + string[:prefix_length][::-1]
