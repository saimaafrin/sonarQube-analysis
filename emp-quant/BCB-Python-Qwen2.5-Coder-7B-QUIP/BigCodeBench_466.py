
import json
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def task_func(my_obj):
    class CustomEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Enum):
                return obj.name
            return super().default(obj)

    return json.dumps(my_obj, cls=CustomEncoder)

result = task_func({'color': Color.RED})
print(result)  # Output: {"color": "RED"}