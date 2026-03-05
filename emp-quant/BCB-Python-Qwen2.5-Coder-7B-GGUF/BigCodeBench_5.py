
import random
import math

def task_func(LETTERS=[chr(i) for i in range(97, 123)]):
    result = {}
    for letter in LETTERS:
        random_integers = [random.randint(0, 100) for _ in range(random.randint(1, 10))]
        mean = sum(random_integers) / len(random_integers)
        variance = sum((x - mean) ** 2 for x in random_integers) / len(random_integers)
        std_dev = math.sqrt(variance)
        result[letter] = std_dev
    return result