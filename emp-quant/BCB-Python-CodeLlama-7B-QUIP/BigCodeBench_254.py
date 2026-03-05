
import json
import math

def task_func(decimal_value, precision=2):
    # Calculate the square root of the decimal value to the given precision
    square_root = math.sqrt(decimal_value, precision)

    # Encode the result as a JSON string
    json_result = json.dumps(square_root)

    return json_result