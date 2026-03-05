from collections import deque
import math
def task_func(l):
    """
    Create a deque from a list, rotate it to the right by 3 positions, and return the deque.
    Also, for demonstration, calculates the square root of the sum of numeric elements in the deque, if there are any, and prints it.
    """
    dq = deque(l)
    dq.rotate(3)
    if any(isinstance(x, (int, float)) for x in dq):
        print(f"The square root of the sum of numeric elements: {math.sqrt(sum(x for x in dq if isinstance(x, (int, float))))}")
    return dq