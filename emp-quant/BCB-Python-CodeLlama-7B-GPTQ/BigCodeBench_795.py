from collections import deque
import math
def task_func(l):
    """
    Create a deque from a list, rotate it to the right by 3 positions, and return the deque.
    Also, for demonstration, calculates the square root of the sum of numeric elements in the deque, if there are any, and prints it.
    >>> task_func([1, 2, 3, 4, 5])
    The square root of the sum of numeric elements: 3.872983346207417
    deque([3, 4, 5, 1, 2])
    """
    dq = deque(l)
    dq.rotate(3)
    numeric_elements = [element for element in dq if isinstance(element, (int, float))]
    if numeric_elements:
        sum_of_numeric_elements = sum(numeric_elements)
        square_root = math.sqrt(sum_of_numeric_elements)
        print(f"The square root of the sum of numeric elements: {square_root}")
    return dq