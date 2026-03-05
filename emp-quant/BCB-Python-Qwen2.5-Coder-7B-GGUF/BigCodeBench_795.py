
from collections import deque
import math

def task_func(l):
    # Create a deque from the input list
    dq = deque(l)
    
    # Rotate the deque to the right by 3 positions
    dq.rotate(3)
    
    # Calculate the square root of the sum of numeric elements in the deque
    numeric_elements = [x for x in dq if isinstance(x, (int, float))]
    sum_of_elements = sum(numeric_elements)
    square_root = math.sqrt(sum_of_elements) if numeric_elements else 0
    
    # Print the square root of the sum of numeric elements
    print(f"The square root of the sum of numeric elements: {square_root}")
    
    # Return the deque
    return dq