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

    # Initialize empty list of prime words
    prime_words = []
    
    # Split sentence into words
    words = sentence.split(' ')
    
    # Iterate through each word
    for word in words:
        # Check if word is a prime number
        if is_prime(len(word)):
            # Add word to prime_words list
            prime_words.append(word)
    
    # Join words in prime_words list with a space
    return ' '.join(prime_words)
