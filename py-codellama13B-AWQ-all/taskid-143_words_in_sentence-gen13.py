def words_in_sentence(sentence: str) -> str:
    """
    You are given a string representing a sentence,
    the sentence contains some words separated by a space,
    and you have to return a string that contains the words from the original sentence,
    whose lengths are prime numbers,
    the order of the words in the new string should be the same as the original one.

    Example 1:
    >>> words_in_sentence('This is a test')
    'is'

    Example 2:
    >>> words_in_sentence('lets go for swimming')
    'go for'
    
    Constraints:
        * 1 <= len(sentence) <= 100
        * sentence contains only letters
    """


    # first, we have to split the string into a list of words
    # and check if they are prime numbers
    words = sentence.split(" ")
    prime_numbers = []
    for word in words:
        word_length = len(word)
        if is_prime(word_length):
            prime_numbers.append(word)

    # then, we have to join all the prime words into a string
    return " ".join(prime_numbers)
