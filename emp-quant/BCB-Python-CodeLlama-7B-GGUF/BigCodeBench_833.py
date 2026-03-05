
import random
from collections import Counter
from statistics import mode

def task_func(list_length=1000, range_start=1, range_end=10, random_seed=None):
    if random_seed is not None:
        random.seed(random_seed)
    numbers = random.sample(range(range_start, range_end+1), list_length)
    counter = Counter(numbers)
    mode_value = mode(numbers)
    return (mode_value, (number, counter[number]) for number in numbers)

mode, numbers = task_func(20, -12, 334, random_seed=23)
print(mode)
print([(number, counter[number]) for number in numbers])