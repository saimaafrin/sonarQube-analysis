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

    # In Python strings are immutable, so we don't want to modify them.
    # We just want to build a new string based on supplied one.
    # So let's just convert it to list of characters.
    string = list(string)

    # This function reverses list in place.
    # Note that it mutates the list, so it is not pure.
    def reverse(arr: list) -> None:
        length = len(arr)
        for i in range(length // 2):
            arr[i], arr[length - 1 - i] = arr[length - 1 - i], arr[i]

    # Find the longest postfix of a string that is a palindrome.
    suffix = []
    for i in range(len(string), 0, -1):
        if string[:i] == string[len(string) - i :]:
            suffix = string[:i]
            break

    # Reverse prefix of a string that comes before the palindromic suffix.
    prefix = string[len(suffix) :]
    reverse(prefix)

    # Join palindromic suffix with reversed prefix and return result.
    return ''.join(suffix + prefix)
