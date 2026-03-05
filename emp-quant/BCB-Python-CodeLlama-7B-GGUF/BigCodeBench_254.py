
import json
import math

def task_func(decimal_value, precision=2):
    """
    Calculate the square root of the given decimal value to a certain precision and then encode the result as a JSON string.

    Args:
        decimal_value (float): The decimal value to calculate the square root of.
        precision (int, optional): The number of decimal places to round the result to. Defaults to 2.

    Returns:
        str: The square root of the decimal value encoded as a JSON string.
    """
    result = math.sqrt(decimal_value)
    result = round(result, precision)
    result = json.dumps(result)
    return result