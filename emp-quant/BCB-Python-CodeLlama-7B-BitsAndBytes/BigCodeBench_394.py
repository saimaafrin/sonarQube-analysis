
import collections
import string
import random

def task_func(length, seed=0):
    # Generate a random string of the given length using ASCII letters
    random.seed(seed)
    random_string = ''.join(random.choice(string.ascii_letters) for _ in range(length))

    # Calculate the frequency of each character in the generated string
    char_freq = collections.Counter(random_string)

    # Output the frequency of each character in the generated string
    print(char_freq)