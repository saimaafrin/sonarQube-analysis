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

    vowels = {'a', 'e', 'i', 'o', 'u', 'y'}
    vowel_count = 0
    for c in s:
        if c.lower() in vowels:
            vowel_count += 1
    return vowel_count
