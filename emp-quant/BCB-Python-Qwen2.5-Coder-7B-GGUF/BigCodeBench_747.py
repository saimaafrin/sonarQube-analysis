
import re
import math

def task_func(s):
    # Split the string by commas
    elements = s.split(',')
    
    # Initialize counters and sum
    count = 0
    sqrt_sum = 0.0
    
    # Regular expression to match integers and floating-point numbers
    number_pattern = re.compile(r'^-?\d+(\.\d+)?$')
    
    for element in elements:
        # Strip whitespace
        element = element.strip()
        
        # Check if the element is a number
        if number_pattern.match(element):
            # Convert to float
            number = float(element)
            # Increment count
            count += 1
            # Add square root to sum
            sqrt_sum += math.sqrt(number)
    
    return count, sqrt_sum