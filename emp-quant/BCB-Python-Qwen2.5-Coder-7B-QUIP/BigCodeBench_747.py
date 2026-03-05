
import re
import math

def task_func(s):
    # Split the input string by commas to get individual elements
    elements = s.split(',')
    
    # Initialize counters and sums
    count = 0
    sqrt_sum = 0.0
    
    # Regular expression to match integers and floating-point numbers
    num_pattern = re.compile(r'^-?\d+(\.\d+)?$')
    
    # Iterate over each element in the list
    for element in elements:
        # Strip whitespace from the element
        element = element.strip()
        
        # Check if the element is a number (integer or float)
        if num_pattern.match(element):
            # Convert the element to a float and increment the count
            num = float(element)
            count += 1
            # Add the square root of the number to the sum
            sqrt_sum += math.sqrt(num)
    
    # Return the count and the sum of square roots
    return count, sqrt_sum