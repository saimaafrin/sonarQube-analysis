
import json
from datetime import datetime
from decimal import Decimal

def task_func(my_obj):
    def custom_serializer(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        raise TypeError(f"Type {type(obj)} not serializable")

    return json.dumps(my_obj, default=custom_serializer)