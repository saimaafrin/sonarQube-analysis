import re
import math
def task_func(s):
    # Split the input string by commas
    elements = s.split(',')
    
    # Initialize count and sum of square roots
    count = 0
    sqrt_sum = 0.0
    
    # Iterate through each element in the list
    for element in elements:
        # Check if the element is a valid integer or float
        if re.match(r"^-?\d+(\.\d+)?$", element):
            # Convert the element to a float
            num = float(element)
            # Increment the count
            count += 1
            # Add the square root of the number to the sum
            sqrt_sum += math.sqrt(num)
    
    # Return the count and the sum of square roots
    return count, sqrt_sum