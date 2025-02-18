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

    string_length = len(string)
    palindromic_postfix = ''
    # Find the longest palindromic suffix of a supplied string
    for index in range(1, string_length):
        if string[:index] == string[:index][::-1]:
            palindromic_postfix = string[index:]
    # Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    if palindromic_postfix:
        return string + palindromic_postfix[::-1]
    return string
