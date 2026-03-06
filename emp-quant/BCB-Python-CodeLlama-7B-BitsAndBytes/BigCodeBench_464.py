
import json
from datetime import datetime
from decimal import Decimal

def task_func(my_obj):
    class JSONEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, datetime):
                return o.isoformat()
            elif isinstance(o, Decimal):
                return float(o)
            else:
                return super(JSONEncoder, self).default(o)

    return json.dumps(my_obj, cls=JSONEncoder)