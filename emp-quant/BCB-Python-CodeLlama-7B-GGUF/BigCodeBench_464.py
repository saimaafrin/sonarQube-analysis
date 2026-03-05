
import json
from datetime import datetime
from decimal import Decimal

def task_func(my_obj):
    class MyEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, Decimal):
                return float(obj)
            else:
                return super(MyEncoder, self).default(obj)

    return json.dumps(my_obj, cls=MyEncoder)

task_func({'name': 'Alice', 'age': 30})