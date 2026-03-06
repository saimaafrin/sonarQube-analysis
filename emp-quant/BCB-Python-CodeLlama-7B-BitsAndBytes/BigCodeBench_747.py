
import re
import math

def task_func(s):
    # Split the string into a list of tokens using regex
    tokens = re.split(r'\s*,\s*', s)

    # Initialize counters for integers and floats
    int_count = 0
    float_count = 0

    # Initialize sum for square roots
    sqrt_sum = 0.0

    # Iterate over the tokens and check if they are integers or floats
    for token in tokens:
        try:
            # Try to convert the token to an integer
            int(token)
            int_count += 1
        except ValueError:
            # If the token is not an integer, try to convert it to a float
            try:
                float(token)
                float_count += 1
            except ValueError:
                # If the token is not a float, it is neither an integer nor a float
                pass

        # Calculate the square root of the token and add it to the sum
        sqrt_sum += math.sqrt(float(token))

    # Return the count and sum of square roots
    return int_count, float_count, sqrt_sum