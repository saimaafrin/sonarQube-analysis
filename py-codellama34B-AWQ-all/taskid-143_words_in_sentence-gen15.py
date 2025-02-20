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

    # Initialize the prime number list
    primes = [2, 3]
    max_num = 100

    # Loop until the sqrt of max_num
    for num in range(5, int(max_num ** 0.5) + 1):
        # Check if num is prime
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:
            # Add the new found prime number to the list
            primes.append(num)

    # Split the sentence into a list of words
    words = sentence.split()
    # Declare an empty list to hold the prime words
    prime_words = []
    # Loop through the words
    for word in words:
        # Check if the length of the word is in the prime list
        if len(word) in primes:
            # Add the word to the prime word list
            prime_words.append(word)
    # Join the prime words with a space
    return ' '.join(prime_words)
