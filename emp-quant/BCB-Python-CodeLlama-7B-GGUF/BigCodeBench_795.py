
from collections import deque
import math

def task_func(l):
    dq = deque(l)
    dq.rotate(3)
    print(f"The square root of the sum of numeric elements: {math.sqrt(sum(i for i in dq if isinstance(i, (int, float))))}")
    return dq

print(task_func([1, 2, 3, 4, 5]))