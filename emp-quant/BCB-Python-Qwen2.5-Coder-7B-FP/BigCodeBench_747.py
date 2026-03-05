import re
import math
def task_func(s):
    # Split the input string by commas
    elements = s.split(',')
    
    # Initialize counters and sum
    count = 0
    sqrt_sum = 0.0
    
    # Regular expression to match integers and floating-point numbers
    number_pattern = re.compile(r'^-?\d+(\.\d+)?$')
    
    # Iterate over each element in the list
    for element in elements:
        # Strip whitespace
        element = element.strip()
        
        # Check if the element is a number
        if number_pattern.match(element):
            # Convert the element to a float
            number = float(element)
            
            # Increment the count
            count += 1
            
            # Add the square root of the number to the sum
            sqrt_sum += math.sqrt(number)
    
    # Return the count and the sum of square roots
    return count, sqrt_sum