import json
from enum import Enum
def task_func(my_obj):
    class CustomJSONEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Enum):
                return obj.name  # or obj.value, depending on your preference
            return super().default(obj)

    return json.dumps(my_obj, cls=CustomJSONEncoder)