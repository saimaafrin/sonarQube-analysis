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

    # Check the string for the longest palindromic postfix
    postfix = longest_postfix_palindromic(string)
    # Find the shortest palindromic prefix
    prefix = shortest_prefix_palindromic(string[:-len(postfix)])
    return string + prefix[::-1]
