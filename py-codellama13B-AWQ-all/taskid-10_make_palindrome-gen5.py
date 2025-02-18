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

    if string == '':
        return string

    # Get longest postfix of supplied string that is a palindrome
    # by comparing the end of the string to its start
    # from the end to the beginning of the string
    # until the first mismatch is found
    # or the end of the string is reached
    #
    # for example for 'catac'
    # 1. find the longest palindrome from 'catac' that is at the end of the string
    # 2. this palindrome is 'c'
    # 3. find the longest palindrome from 'cata' that is at the beginning of the string
    # 4. this palindrome is 't'
    # 5. the longest palindrome that is at the end of the string is 'c'
    # 6. the longest palindrome that is at the beginning of the string is 't'
    # 7. the shortest palindrome that is a prefix of supplied string is 't'
    # 8. the shortest palindrome that is a suffix of supplied string is 'c'
    # 9. the shortest palindrome that begins with supplied string is 'tc'
    # 10. the shortest palindrome that begins with 'tc' is 'tcac'
    # 11. the shortest palindrome that begins with 'cata' is 'catac'
    for i in range(len(string), 0, -1):
        if string[i - 1::-1] == string[:i]:
            palindromic_suffix = string[i - 1::-1]
            break
    else:
        return string

    # The length of the shortest palindrome that begins with supplied string
    # is the length of supplied string plus the length of the palindromic suffix
    #
    # for example for 'catac'
    # 1. find the length of the shortest palindrome that begins with 'cata'
    # 2. the length of the shortest palindrome that begins with 'cata' is 5
    # 3. the length of the shortest palindrome that begins with 'tc' is 4
    # 4. the length of the shortest palindrome that begins with supplied string is 5
    # 5. the shortest palindrome that begins with supplied string is 'catac'
    string_length = len(string)
    palindromic_suffix_length = len(palindromic_suffix)
    shortest_palindrome_length = string_length + palindromic_suffix_length

    # The shortest palindrome that begins with supplied string
    # is a concatenation of supplied string
    # and the reverse of its prefix
    #
    # for example for 'catac'
    # 1. find the shortest palindrome that begins with 'cata'
    # 2. the shortest palindrome that begins with 'cata' is 'catac'
    # 3. find the shortest palindrome that begins with 'tc'
    # 4. the shortest palindrome that begins with 'tc' is 'tcac'
    # 5. the shortest palindrome that begins with supplied string is 'catac'
    shortest_palindrome = string + palindromic_suffix[::-1]

    return shortest_palindrome
