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

    if len(string) == 0:
        return string

    # Reverse input string to find longest palindromic postfix of original string.
    # Then find the length of the postfix and its reverse.
    # That will give us the length of the prefix.
    # Now we can reverse the prefix and append to the original string.
    reverse_postfix = string[::-1]
    palindromic_postfix_length = longest_common_prefix(string, reverse_postfix)
    prefix_length = len(string) - palindromic_postfix_length

    prefix = string[:prefix_length]
    suffix = reverse_postfix[:palindromic_postfix_length]

    return prefix + suffix
