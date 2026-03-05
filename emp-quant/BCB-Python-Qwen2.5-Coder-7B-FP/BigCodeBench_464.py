import json
from datetime import datetime
from decimal import Decimal
def task_func(my_obj):
    """
    Serializes an object to a JSON string, adding support for datetime and Decimal data types.
    
    Args:
    my_obj (dict): The dictionary to serialize.
    
    Returns:
    str: A JSON-formatted string representing `my_obj`, with datetime and Decimal objects properly serialized.
    """
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, Decimal):
                return str(obj)
            return super().default(obj)
    
    return json.dumps(my_obj, cls=CustomEncoder)