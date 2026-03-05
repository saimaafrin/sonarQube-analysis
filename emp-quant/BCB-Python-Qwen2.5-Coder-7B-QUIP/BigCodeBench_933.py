
import string
import wordninja

def task_func(word):
    alphabet_position = {letter: idx for idx, letter in enumerate(string.ascii_lowercase, start=1)}
    word_list = wordninja.split(word)
    result = []
    for word in word_list:
        word_result = []
        for letter in word:
            if letter in alphabet_position:
                word_result.append((letter, alphabet_position[letter]))
        result.append(word_result)
    return result