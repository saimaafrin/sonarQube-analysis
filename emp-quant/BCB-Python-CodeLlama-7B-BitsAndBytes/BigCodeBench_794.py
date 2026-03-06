
import string
import random

BRACKETS = "(){}[]"

def task_func(length, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    str = ""
    for i in range(length):
        if random.random() < 0.5:
            str += BRACKETS[random.randint(0, 3)]
        else:
            str += random.choice(string.ascii_lowercase)
    return str

string = task_func(34, random_seed=42)
print(string)