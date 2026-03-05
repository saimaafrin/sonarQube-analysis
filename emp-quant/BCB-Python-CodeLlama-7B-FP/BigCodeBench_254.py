import json
import math
def task_func(decimal_value, precision=2):
    """
    Calculate the square root of the given decimal value to a certain precision and then encode the result as a JSON string.
    :param decimal_value: The decimal value to calculate the square root of.
    :param precision: The precision to which the square root should be calculated.
    :return: The square root of the decimal value encoded as a JSON string.
    """
    # Calculate the square root of the decimal value to the specified precision
    square_root = math.sqrt(decimal_value, precision)

    # Encode the square root as a JSON string
    json_string = json.dumps(square_root)

    return json_string
decimal_value = 16
precision = 2