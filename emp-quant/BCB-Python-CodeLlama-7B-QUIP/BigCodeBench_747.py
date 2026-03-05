
import re
import math

def task_func(s):
    # Use regular expressions to extract the numbers from the string
    numbers = re.findall(r"[-+]?\d+", s)

    # Initialize the count and sum variables
    count = 0
    sqrt_sum = 0

    # Loop through the numbers and perform the necessary calculations
    for number in numbers:
        if number.is_integer():
            count += 1
            sqrt_sum += math.sqrt(int(number))
        else:
            count += 1
            sqrt_sum += math.sqrt(float(number))

    return count, sqrt_sum