
import json
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.name
        return json.JSONEncoder.default(self, obj)

def task_func(my_obj):
    return json.dumps(my_obj, cls=CustomJSONEncoder)