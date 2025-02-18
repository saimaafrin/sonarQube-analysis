from typing import List

def skjkasdkd(lst: List[int]) -> int:
    """You are given a list of integers.
    You need to find the largest prime value and return the sum of its digits.

    Examples:
    >>> skjkasdkd([0, 3, 2, 1, 3, 5, 7, 4, 5, 5, 5, 2, 181, 32, 4, 32, 3, 2, 32, 324, 4, 3])
    10
    >>> skjkasdkd([1, 0, 1, 8, 2, 4597, 2, 1, 3, 40, 1, 2, 1, 2, 4, 2, 5, 1])
    25
    >>> skjkasdkd([1, 3, 1, 32, 5107, 34, 83278, 109, 163, 23, 2323, 32, 30, 1, 9, 3])
    13
    >>> skjkasdkd([0, 724, 32, 71, 99, 32, 6, 0, 5, 91, 83, 0, 5, 6])
    11
    >>> skjkasdkd([0, 81, 12, 3, 1, 21])
    3
    >>> skjkasdkd([0, 8, 1, 2, 1, 7])
    7
    """

    if not lst: return 0
    mx = max(lst)
    #print(mx)
    primes = [True] * (mx+1)
    primes[0] = primes[1] = False
    for i in range(2, int(mx ** 0.5)+1):
        if primes[i]:
            primes[i*i::i] = [False] * len(primes[i*i::i])
    lst = [i for i in lst if primes[i]]
    #print(lst)
    #lst = lst[0]
    return sum([int(str(i)) for i in lst])
