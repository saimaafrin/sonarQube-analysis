import json
from enum import Enum
def task_func(my_obj):
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Enum):
                return obj.name
            return json.JSONEncoder.default(self, obj)

    return json.dumps(my_obj, cls=CustomJSONEncoder)