import json
from datetime import datetime
import numpy as np
from decimal import Decimal
def task_func(my_obj):
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, datetime):
                return obj.isoformat()
            elif isinstance(obj, np.ndarray):
                return obj.tolist()
            elif isinstance(obj, Decimal):
                return float(obj)
            else:
                raise TypeError("Object of type '{}' is not JSON serializable".format(type(obj)))

    return json.dumps(my_obj, cls=CustomJSONEncoder)