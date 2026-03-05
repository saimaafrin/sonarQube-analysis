import re
import math
def task_func(s):
    """
    Count the number of integers and floating-point numbers in a comma-separated string and calculate the sum of their square roots.
    """
    # Split the string into a list of substrings using the comma as a delimiter
    substrings = s.split(",")

    # Initialize the count of integers and floats to 0
    int_count = 0
    float_count = 0

    # Initialize the sum of the square roots of the integers and floats to 0
    sqrt_sum = 0

    # Iterate over the substrings
    for substring in substrings:
        # Check if the substring is an integer
        if re.match(r"^-?\d+$", substring):
            # Increment the count of integers
            int_count += 1

            # Calculate the square root of the integer
            sqrt_sum += math.sqrt(int(substring))

        # Check if the substring is a floating-point number
        elif re.match(r"^-?\d+\.\d+$", substring):
            # Increment the count of floats
            float_count += 1

            # Calculate the square root of the floating-point number
            sqrt_sum += math.sqrt(float(substring))

    # Return the count of integers and floats and the sum of their square roots
    return int_count, float_count, sqrt_sum