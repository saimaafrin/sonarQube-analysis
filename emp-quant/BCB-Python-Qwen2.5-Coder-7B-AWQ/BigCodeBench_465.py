import json
from datetime import datetime
import numpy as np
from decimal import Decimal
class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, Decimal):
            return float(obj)
        return super().default(obj)
def task_func(my_obj):
    try:
        return json.dumps(my_obj, cls=CustomJSONEncoder)
    except TypeError as e:
        raise TypeError("Unsupported type encountered during serialization") from e