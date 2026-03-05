from collections import deque
import math
def task_func(l):
    """
    Create a deque from a list, rotate it to the right by 3 positions, and return the deque.
    Also, calculate the square root of the sum of numeric elements in the deque, if there are any, and print it.
    
    Args:
    l (list): The input list to be converted into a deque and rotated.
    
    Returns:
    dq (collections.deque): A deque obtained from the input list after performing a right rotation by 3 positions.
    """
    # Create a deque from the input list
    dq = deque(l)
    
    # Rotate the deque to the right by 3 positions
    dq.rotate(3)
    
    # Calculate the sum of numeric elements in the deque
    numeric_sum = sum(item for item in dq if isinstance(item, (int, float)))
    
    # Calculate the square root of the sum
    square_root = math.sqrt(numeric_sum) if numeric_sum > 0 else 0
    
    # Print the square root of the sum
    print(f"The square root of the sum of numeric elements: {square_root}")
    
    # Return the rotated deque
    return dq