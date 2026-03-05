
import random
import re

def task_func(text, seed=None):
    # Set the seed for the random number generator for reproducibility
    if seed is not None:
        random.seed(seed)

    # Define a function to scramble a word
    def scramble_word(word):
        if len(word) > 3:
            # Get the first and last letters
            first = word[0]
            last = word[-1]
            # Get the middle letters as a list
            middle = list(word[1:-1])
            # Shuffle the middle letters
            random.shuffle(middle)
            # Join the shuffled middle letters
            middle = ''.join(middle)
            # Return the scrambled word
            return first + middle + last
        else:
            return word

    # Use regex to find all words in the text
    words = re.findall(r'\b\w+\b', text)
    # Scramble each word
    scrambled_words = [scramble_word(word) for word in words]
    # Replace the original words with the scrambled words
    scrambled_text = re.sub(r'\b\w+\b', lambda match: match.group(0).replace(match.group(0), scrambled_words.pop(0)), text)
    return scrambled_text