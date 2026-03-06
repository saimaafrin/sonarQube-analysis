
import re
import math

def task_func(s):
    # Split the input string by commas to get individual elements
    elements = s.split(',')
    
    # Initialize counters and sums
    count = 0
    sqrt_sum = 0.0
    
    # Regular expression to match integers and floating-point numbers
    number_pattern = re.compile(r'^-?\d+(\.\d+)?$')
    
    for element in elements:
        # Strip any leading/trailing whitespace
        element = element.strip()
        
        # Check if the element is an integer or float using regex
        if number_pattern.match(element):
            # Convert the element to a float
            num = float(element)
            
            # Increment the count
            count += 1
            
            # Add the square root of the number to the sum
            sqrt_sum += math.sqrt(num)
    
    return count, sqrt_sum