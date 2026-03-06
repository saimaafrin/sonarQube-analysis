
import json
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Color):
            return obj.name
        return json.JSONEncoder.default(self, obj)

def task_func(my_obj):
    return json.dumps(my_obj, cls=CustomJSONEncoder)

my_dict = {'name': 'Alice', 'age': 30, 'favorite_color': Color.RED}
print(task_func(my_dict))