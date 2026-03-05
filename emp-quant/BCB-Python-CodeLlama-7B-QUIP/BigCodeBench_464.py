
import json
from datetime import datetime
from decimal import Decimal

def task_func(my_obj):
    def default(o):
        if isinstance(o, datetime):
            return o.isoformat()
        if isinstance(o, Decimal):
            return round(o, 2)
        return o
    return json.dumps(my_obj, default=default)