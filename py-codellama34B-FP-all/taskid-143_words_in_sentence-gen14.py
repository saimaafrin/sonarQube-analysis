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

    # Get a list of words from the sentence
    words = sentence.split()

    # Create a list of prime numbers
    # For this case, we can just use a static list of the first 10 prime numbers
    # but you can use a helper function to generate a list of prime numbers
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

    # Create a list to store the prime words
    prime_words = []

    # Iterate through the list of words
    for word in words:
        # Get the length of the word
        word_length = len(word)

        # Check if the word length is a prime number
        if word_length in primes:
            # Add the word to the list of prime words
            prime_words.append(word)

    # Return the list of prime words as a string
    return " ".join(prime_words)
