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

    # implement your solution here
    words = sentence.split()
    is_prime = [True] * len(words)
    is_prime[0] = False
    for i in range(2, int(len(words) ** 0.5) + 1):
        for j in range(i + i, len(words), i):
            is_prime[j] = False
    return " ".join(word for word, prime in zip(words, is_prime) if prime)
