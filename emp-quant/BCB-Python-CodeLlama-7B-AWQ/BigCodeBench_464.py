import json
from datetime import datetime
from decimal import Decimal
def task_func(my_obj):
    """
    Serializes an object to a JSON string, adding support for datetime and Decimal data types.
    Handle complex data types not natively supported by the json module's default encoder.
    The `My_class` parameter is reserved for future use and does not affect the current implementation.
    Serialize a simple dictionary:
    >>> task_func({'name': 'Alice', 'age': 30})
    '{"name": "Alice", "age": 30}'
    """
    class JSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, Decimal):
                return float(obj)
            else:
                return super(JSONEncoder, self).default(obj)

    return json.dumps(my_obj, cls=JSONEncoder)