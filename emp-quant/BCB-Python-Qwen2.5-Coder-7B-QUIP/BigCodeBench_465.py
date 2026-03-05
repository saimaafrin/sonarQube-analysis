
import json
from datetime import datetime
import numpy as np
from decimal import Decimal
from typing import Any, Union, Dict, List, Tuple, Optional

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, Decimal):
            return str(obj)
        else:
            return super().default(obj)

def task_func(my_obj: Union[Dict, List, Tuple, Any]) -> str:
    try:
        serialized_json = json.dumps(my_obj, cls=CustomJSONEncoder)
        return serialized_json
    except TypeError as e:
        raise TypeError(f"Unsupported type encountered: {e}")