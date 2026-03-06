import re
import math
def task_func(s):
    '''
    Count the number of integers and floating-point numbers in a comma-separated string and calculate the sum of their square roots.

    Parameters:
    - s (str): The comma-separated string.

    Returns:
    - count (int): The number of integers and floats in the string.
    - sqrt_sum (float): The sum of the square roots of the integers and floats.
    
    Requirements:
    - re
    - math
    
    Example:
    >>> count, sqrt_sum = task_func('1,2,3.5,abc,4,5.6')
    >>> print(count)  # Ensure this matches exactly with expected output
    5
    >>> print("{:.2f}".format(sqrt_sum))  # Ensure this matches exactly with expected output
    8.65
    '''
    # Your code here
    count = 0
    sqrt_sum = 0
    for i in re.split(r',', s):
        try:
            count += 1
            sqrt_sum += math.sqrt(float(i))
        except ValueError:
            pass
    return count, sqrt_sum