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


    # Initialize a list for storing the prime words
    prime_words = []

    # Initialize a list for storing the non-prime words
    non_prime_words = []

    # Initialize a list for storing the lengths of words
    lengths = []

    # Split the sentence into words
    words = sentence.split()

    # Iterate over the words
    for word in words:
        # Calculate the length of the word
        length = len(word)

        # If the length of the word is prime
        if is_prime(length):
            # Add the word to the prime_words list
            prime_words.append(word)
        else:
            # Add the word to the non_prime_words list
            non_prime_words.append(word)

        # Add the length of the word to the lengths list
        lengths.append(length)

    # Create a string from the prime words
    prime_string = ' '.join(prime_words)

    # Create a string from the non-prime words
    non_prime_string = ' '.join(non_prime_words)

    # Return the concatenation of the prime string and the non-prime string
    return prime_string + ' ' + non_prime_string
