import json
import math
def task_func(decimal_value, precision=2):
    """
    Calculate the square root of the given decimal value to a certain precision and then encode the result as a JSON string.
    :param decimal_value: The decimal value to calculate the square root of.
    :param precision: The precision to which the square root should be calculated.
    :return: The square root of the decimal value encoded as a JSON string.
    """
    # Calculate the square root of the decimal value
    square_root = math.sqrt(decimal_value)

    # Round the square root to the specified precision
    rounded_square_root = round(square_root, precision)

    # Encode the rounded square root as a JSON string
    json_string = json.dumps(rounded_square_root)

    return json_string