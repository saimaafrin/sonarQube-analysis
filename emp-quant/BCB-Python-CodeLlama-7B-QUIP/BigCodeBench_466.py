
import json
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

def task_func(my_obj):
    class ColorEncoder(json.JSONEncoder):
        def default(self, obj):
            if isinstance(obj, Color):
                return obj.name
            return super().default(obj)
    return json.dumps(my_obj, cls=ColorEncoder)

my_obj = {'name': 'Alice', 'age': 30, 'color': Color.RED}
print(task_func(my_obj))