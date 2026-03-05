import json
from datetime import datetime
from decimal import Decimal
def task_func(my_obj):
    """
    Serializes an object to a JSON string, adding support for datetime and Decimal data types.
    Handles complex data types not natively supported by the json module's default encoder.
    
    Args:
    my_obj (dict): The dictionary to be serialized.
    
    Returns:
    str: A JSON-formatted string representing `my_obj`, with datetime and Decimal objects properly serialized.
    """
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, Decimal):
                return float(obj)
            return super().default(obj)
    
    return json.dumps(my_obj, cls=CustomEncoder)