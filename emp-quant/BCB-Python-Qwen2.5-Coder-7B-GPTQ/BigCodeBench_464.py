import json
from datetime import datetime
from decimal import Decimal
def task_func(my_obj):
    # Custom JSON encoder to handle datetime and Decimal types
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, Decimal):
                return float(obj)
            return super().default(obj)
    
    # Serialize the object using the custom encoder
    return json.dumps(my_obj, cls=CustomEncoder)