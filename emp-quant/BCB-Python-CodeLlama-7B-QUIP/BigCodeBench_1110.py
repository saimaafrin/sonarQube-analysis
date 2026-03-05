
from collections import Counter
from operator import itemgetter
import itertools

def task_func(word_dict):
    counter = Counter()
    for word in word_dict:
        counter.update(word)
    return counter.most_common()