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

    def is_palindrome(word: str) -> bool:
        return word == word[::-1]

    def find_palindromic_suffix(word: str) -> str:
        for suffix_length in range(len(word), 0, -1):
            suffix = word[-suffix_length:]
            if is_palindrome(suffix):
                return suffix
        return ''

    palindromic_suffix = find_palindromic_suffix(string)
    return string + palindromic_suffix[::-1]
