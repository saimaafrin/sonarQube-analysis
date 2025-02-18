def vowels_count(s: str) -> int:
    """Write a function vowels_count which takes a string representing
    a word as input and returns the number of vowels in the string.
    Vowels in this case are 'a', 'e', 'i', 'o', 'u'. Here, 'y' is also a
    vowel, but only when it is at the end of the given word.

    Example:
    >>> vowels_count('abcde')
    2
    >>> vowels_count('ACEDY')
    3
    """

    vowels_count = 0
    for vowel in s:
        if vowel == 'a' or vowel == 'e' or vowel == 'i' or vowel == 'o' or vowel == 'u' or vowel == 'A' or vowel == 'E' or vowel == 'I' or vowel == 'O' or vowel == 'U':
            vowels_count += 1
        if vowel == 'y' and s[-1] != 'y':
            vowels_count += 1
    return vowels_count
