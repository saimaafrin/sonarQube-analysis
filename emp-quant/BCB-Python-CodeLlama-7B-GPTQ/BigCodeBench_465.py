import json
from datetime import datetime
import numpy as np
from decimal import Decimal
def task_func(my_obj):
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, datetime):
                return o.isoformat()
            elif isinstance(o, np.ndarray):
                return o.tolist()
            elif isinstance(o, Decimal):
                return float(o)
            else:
                raise TypeError("Object of type {} is not JSON serializable".format(type(o)))

    return json.dumps(my_obj, cls=CustomJSONEncoder)