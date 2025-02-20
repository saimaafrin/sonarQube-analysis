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

    reversed = string[::-1]
    # find the length of the longest postfix of string that is a palindrome
    # we can find that by finding the first non-matching character and using its index
    first_non_match = next((i for i, chars in enumerate(zip(string, reversed)) if chars[0] != chars[1]), len(string))
    return string + reversed[:first_non_match][::-1]
