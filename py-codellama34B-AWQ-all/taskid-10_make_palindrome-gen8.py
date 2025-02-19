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

    # first, we need to find the first non-palindrome character from the center
    # to do this, we can use palindromic properties
    # let's assume that we have a palindrome of even length
    # in this case, the palindrome is symmetric to the center
    # and we can safely say that it's first non-palindrome character is in the middle
    # so we can take the middle character of the string
    # and check if it's the same as the character to the right of it
    # if it is, then we need to check the previous character
    # if it's not, then we can say that the first non-palindrome character is at the current position
    # we can use this idea recursively to find the first non-palindrome character
    # but we need to check the case when our palindrome is of odd length
    # in this case, the first non-palindrome character is clearly in the middle
    # so we can take it as is and then recursively check the characters to the left and to the right
    # we can also assume that the string is not empty
    # so we don't need to check the case when the string is empty
    # the code will look like this
    length = len(string)
    if length == 1:
        return string + string[::-1]
    middle = length // 2
    if string[middle] == string[-middle - 1]:
        # we need to check the character to the left
        # because the character to the right is the same as the character to the left
        if string[middle - 1] == string[-middle]:
            # we need to check one more character to the left
            # because the character to the left is the same as the character to the right
            return string + string[length - middle - 2::-1]
        return string + string[length - middle - 1::-1]
    # in this case, the character in the middle is different from the character to the right
    # so we can say that the first non-palindrome character is clearly in the middle
    return string + string[length - middle - 1::-1]
