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

    vowels = ['a', 'e', 'i', 'o', 'u']
    word = s.lower()
    vowels_num = 0

    for vowel in vowels:
        if vowel in word:
            vowels_num += word.count(vowel)
        if vowel == 'y' and word[-1] == 'y':
            vowels_num += 1
    return vowels_num
