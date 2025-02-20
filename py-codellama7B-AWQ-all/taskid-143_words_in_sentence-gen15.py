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

    # TODO: Write a more efficient algorithm,
    #       which has a time complexity of O(n) and a space complexity of O(1)
    #       where n is the length of the input string sentence

    words = sentence.split(" ")

    prime_words = [word for word in words if is_prime(len(word))]

    return " ".join(prime_words)
