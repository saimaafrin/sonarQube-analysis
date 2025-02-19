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


    # Base case.
    if len(string) < 2:
        return string + string[::-1]

    # Find the longest postfix that is a palindrome.
    left, right = 0, len(string) - 1
    while left < right and string[left] == string[right]:
        left += 1
        right -= 1

    # If we found a palindrome, then just add the reverse of the prefix to it.
    # Otherwise, the whole string is our palindrome.
    if left >= right:
        return string + string[::-1]

    # Find the first character that comes before the palindromic suffix and is different from it.
    for i in range(left - 1, -1, -1):
        if string[i] != string[right]:
            return string + string[i + 1 : left + 1] + string[::-1]

    return string + string[::-1]
