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

    reversed_string = string[::-1]
    longest_palindrome = string
    for idx in range(len(string) - 1, -1, -1):
        if string[idx:] == reversed_string[:len(string) - idx]:
            longest_palindrome = string[idx:]
            break
    return longest_palindrome + reversed_string[:len(string) - idx]
