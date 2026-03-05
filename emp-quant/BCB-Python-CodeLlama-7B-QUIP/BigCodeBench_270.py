
import re
from collections import Counter

def task_func(sentence):
    words = re.findall(r'\w+', sentence)
    counts = Counter(words)
    return dict(counts)