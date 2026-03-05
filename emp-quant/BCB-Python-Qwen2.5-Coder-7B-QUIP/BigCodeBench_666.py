
from itertools import combinations
import math

def task_func(seq, letter_weight_dict):
    def calculate_weight(subseq):
        return sum(letter_weight_dict[letter] for letter in subseq)

    max_weight = -math.inf
    best_subseq = ""

    for length in range(1, len(seq) + 1):
        for subseq in combinations(seq, length):
            subseq = ''.join(subseq)
            weight = calculate_weight(subseq)
            if weight > max_weight:
                max_weight = weight
                best_subseq = subseq

    return str(best_subseq)