import json
import math
def task_func(decimal_value, precision=2):
    # Calculate the square root of the given decimal value
    sqrt_value = round(math.sqrt(decimal_value), precision)
    
    # Encode the result as a JSON string
    json_result = json.dumps(sqrt_value)
    
    return json_result