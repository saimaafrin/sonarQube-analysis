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

    palindromic_postfix_len = 1  # length of the longest palindromic suffix
    palindromic_postfix_start_index = 0  # index of the start of the longest palindromic suffix

    for i in range(len(string)):
        for j in range(palindromic_postfix_len, 0, -1):
            if string[i - j + 1: i + 1] == string[i - j + 1: i + 1][::-1]:
                palindromic_postfix_len = j
                palindromic_postfix_start_index = i - j + 1
                break
        if palindromic_postfix_len == len(string) - i:
            break
    return string + string[:palindromic_postfix_start_index][::-1]
