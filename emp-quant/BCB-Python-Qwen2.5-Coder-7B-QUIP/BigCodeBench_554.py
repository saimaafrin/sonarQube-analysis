
import numpy as np
import random

def task_func(MIN_WORDS, MAX_WORDS, WORDS_POOL):
    # Generate a random number of words within the specified range
    num_words = random.randint(MIN_WORDS, MAX_WORDS)
    
    # Randomly select words from the WORDS_POOL
    words = [random.choice(WORDS_POOL) for _ in range(num_words)]
    
    # Shuffle the list of words to ensure randomness
    random.shuffle(words)
    
    # Join the words to form a sentence
    sentence = ' '.join(words)
    
    # Reverse the sentence to create the palindrome
    palindrome_sentence = f"{sentence} {sentence[::-1]}"
    
    return palindrome_sentence