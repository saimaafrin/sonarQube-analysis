import json
from enum import Enum
def task_func(my_obj):
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, Enum):
                return o.name
            return json.JSONEncoder.default(self, o)

    return json.dumps(my_obj, cls=CustomJSONEncoder)