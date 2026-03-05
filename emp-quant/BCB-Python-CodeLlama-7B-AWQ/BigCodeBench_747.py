import re
import math
def task_func(s):
    """
    Count the number of integers and floating-point numbers in a comma-separated string and calculate the sum of their square roots.

    Args:
        s (str): A comma-separated string of integers and floating-point numbers.

    Returns:
        count (int): The number of integers and floats in the string.
        sqrt_sum (float): The sum of the square roots of the integers and floats.
    """
    # Split the string into a list of numbers using the comma as a delimiter
    numbers = s.split(",")

    # Initialize the count and sum variables
    count = 0
    sqrt_sum = 0.0

    # Iterate over the list of numbers and check if each is an integer or a float
    for number in numbers:
        try:
            # If the number is an integer, increment the count and add its square root to the sum
            count += 1
            sqrt_sum += math.sqrt(int(number))
        except ValueError:
            # If the number is not an integer, try to convert it to a float and add its square root to the sum
            try:
                count += 1
                sqrt_sum += math.sqrt(float(number))
            except ValueError:
                # If the number cannot be converted to a float, ignore it
                pass

    # Return the count and sum
    return count, sqrt_sum