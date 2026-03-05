
from collections import deque
import math

def task_func(l):
    # Create a deque from the input list
    dq = deque(l)
    
    # Rotate the deque to the right by 3 positions
    dq.rotate(3)
    
    # Calculate the square root of the sum of numeric elements in the deque
    numeric_sum = sum(x for x in dq if isinstance(x, (int, float)))
    sqrt_sum = math.sqrt(numeric_sum)
    
    # Print the result
    print(f"The square root of the sum of numeric elements: {sqrt_sum}")
    
    # Return the deque
    return dq