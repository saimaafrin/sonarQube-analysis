
import re
import math

def task_func(s):
    # Split the string into a list of tokens using the comma as a delimiter
    tokens = s.split(',')

    # Initialize the count of integers and floats to 0
    int_count = 0
    float_count = 0

    # Initialize the sum of the square roots of the integers and floats to 0
    sqrt_sum = 0

    # Iterate over the tokens and check if they are integers or floats
    for token in tokens:
        if re.match(r'^-?\d+$', token):
            int_count += 1
            sqrt_sum += math.sqrt(int(token))
        elif re.match(r'^-?\d+\.\d+$', token):
            float_count += 1
            sqrt_sum += math.sqrt(float(token))

    # Return the count of integers and floats and the sum of their square roots
    return int_count, float_count, sqrt_sum