
import string
import wordninja

def task_func(word):
    # Convert the word to a list of tuples, with each tuple containing a lowercase English letter and its position in the alphabet
    letter_positions = [(letter, string.ascii_lowercase.index(letter)) for letter in word]

    # Split the given word into a list of words
    words = wordninja.split(word)

    # Output the list of tuples and the list of words
    print(letter_positions)
    print(words)