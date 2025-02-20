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

    # Create list of all words from sentence
    words = sentence.split(" ")

    # Create list of prime numbers
    prime_numbers = []

    for i in range(2, len(words)):
        is_prime = True
        for j in range(2, i):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers.append(i)

    # Create list of prime numbers words
    prime_numbers_words = []
    for i, word in enumerate(words):
        if len(word) in prime_numbers:
            prime_numbers_words.append(word)

    return " ".join(prime_numbers_words)
