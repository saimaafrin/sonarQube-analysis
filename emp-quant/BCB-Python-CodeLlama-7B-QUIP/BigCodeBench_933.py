
import string
import wordninja

def task_func(word):
    # Convert the word to a list of tuples, with each tuple containing a lowercase English letter from the word and its position in the alphabet
    tuples = [(letter, string.ascii_lowercase.index(letter)) for letter in word]
    return tuples

# Split the given word into a list of words
words = wordninja.split(word)

# Output the list of tuples
print(task_func(words))