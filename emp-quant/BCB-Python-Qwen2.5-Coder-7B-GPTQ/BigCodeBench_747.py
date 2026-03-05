import re
import math
def task_func(s):
    # Split the string by commas to get individual numbers
    numbers = s.split(',')
    count = 0
    sqrt_sum = 0.0
    
    # Iterate through each number in the list
    for num in numbers:
        # Check if the number is an integer or a float
        if re.match(r"^-?\d+(\.\d+)?$", num):
            # Convert the number to float
            num = float(num)
            # Increment the count
            count += 1
            # Add the square root of the number to the sum
            sqrt_sum += math.sqrt(num)
    
    # Return the count and the sum of square roots
    return count, sqrt_sum