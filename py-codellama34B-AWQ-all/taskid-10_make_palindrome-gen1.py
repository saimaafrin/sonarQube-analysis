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

    # Step 1: find longest postfix that is a palindrome
    prefix_len = 0
    while prefix_len < len(string):
        if string == string[::-1]:
            break
        prefix_len += 1
    else:
        raise ValueError(f"Can't make a palindrome from {string}")

    # Step 2: append reverse of the prefix to the palindromic suffix
    suffix = string[prefix_len:]
    prefix = string[:len(string) - prefix_len]
    return suffix + prefix[::-1]
