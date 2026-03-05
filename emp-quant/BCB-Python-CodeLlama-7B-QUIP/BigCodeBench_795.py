
from collections import deque
import math

def task_func(l):
    dq = deque(l)
    dq.rotate(3)
    if any(isinstance(x, (int, float)) for x in dq):
        sum_numeric = sum(x for x in dq if isinstance(x, (int, float)))
        sqrt = math.sqrt(sum_numeric)
        print(f"The square root of the sum of numeric elements: {sqrt}")
    return dq

l = [1, 2, 3, 4, 5]
dq = task_func(l)
print(f"deque({l})")
print(f"The deque after rotation: {dq}")