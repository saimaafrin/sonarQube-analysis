
import itertools
from random import shuffle

def task_func(numbers=list(range(1, 3))):
    shuffled_numbers = list(numbers)
    shuffle(shuffled_numbers)
    sums = []
    for i in range(len(shuffled_numbers) - 1):
        sums.append(sum([abs(shuffled_numbers[i] - shuffled_numbers[i + 1])])
    return sum(sums) / len(sums)