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

    # Edge case: empty string is a palindrome by definition
    if not string:
        return string

    # 1. Find the longest postfix of a string that is a palindrome.
    #    E.g. for 'abcdab' the answer is 'bab'.
    #    Use KMP algorithm: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
    #    It finds the longest proper prefix of a string that matches its proper suffix.
    #    Proper prefix is a prefix of a string that doesn't include the first character.
    #    E.g. for 'abcdab' the proper prefixes are '', 'a', 'ab', 'abc', 'abcd'.
    #         Proper suffixes are '', 'b', 'cd', 'dab'.
    #         The proper prefix that matches suffix 'b' is 'a'.
    #    Algorithm compares proper prefixes and proper suffixes to find the longest match.
    #    It runs in O(N) time and O(N) space, where N is the length of the string.
    #    The search starts from the beginning of the string and continues until the end is reached.
    #    It looks for the longest prefix that is a suffix of the string.
    #    It builds a table of shifts for each prefix and then uses the table to find the longest match.
    #    The shifts table is an array of integers, where each integer is a number of steps to take
    #    to find the next character that is a part of a suffix.
    #    E.g. for 'abcdab' the shifts table would look like:
    #         [0, 1, 0, 0, 1, 2, 3]
    #         ^  ^  ^  ^  ^  ^  ^
    #         a  b  c  d  a  b  c
    #    E.g. for 'aabcaca' the shifts table would look like:
    #         [0, 1, 0, 1, 2, 0, 1, 2, 3, 3, 3]
    #         ^  ^  ^  ^  ^  ^  ^  ^  ^  ^  ^
    #         a  a  b  c  a  c  a  c  a  a  c

    shifts = _kmp_build_shifts(string)
    palindromic_suffix_length = _kmp_find_longest_proper_suffix(string, shifts)

    # 2. Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    #    E.g. for 'abcdab' the palindromic suffix is 'bab', so the answer is 'catac'.
    #         Prefix that comes before the palindromic suffix is 'abcd'.
    #         Reverse of the prefix is 'dcba', so the final answer is 'abcdcba'.
    #    For 'cata' the palindromic suffix is 'ata', so the answer is 'catac'.
    #    For 'catac' the palindromic suffix is 'atac', so the answer is 'catac'.

    prefix = string[:len(string) - palindromic_suffix_length]
    return prefix + prefix[::-1]
