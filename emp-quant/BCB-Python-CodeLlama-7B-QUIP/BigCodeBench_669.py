
import itertools
import math

def task_func(x):
    # Find the key pair with the highest sum of the cosine of their values
    key_pair = None
    max_sum = -1
    for key1, value1 in x.items():
        for key2, value2 in x.items():
            if key1 != key2:
                cos_sum = 0
                for i in range(len(value1)):
                    cos_sum += math.cos(value1[i] - value2[i])
                if cos_sum > max_sum:
                    max_sum = cos_sum
                    key_pair = (key1, key2)
    return key_pair