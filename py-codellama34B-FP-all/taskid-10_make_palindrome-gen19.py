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
    if n == 0:
        return ''

    suffix_start = 0

    for i in range(n):
        # Check if i-th character is equal to the first character
        # If so, it might be the end of the palindromic suffix
        if string[i] == string[0]:
            # Then check if there is a palindrome between 0 and i
            j = 1
            while j < i and string[j] == string[i - j]:
                j += 1
            if j == i:
                suffix_start = i

    return string + string[suffix_start + 1: 0:-1]
