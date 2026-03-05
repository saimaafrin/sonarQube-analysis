
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
        else:
            raise TypeError("Unsupported type: {}".format(type(obj)))

def task_func(my_obj):
    return json.dumps(my_obj, cls=CustomJSONEncoder)

# Dictionary with datetime, numpy.ndarray, and Decimal objects
my_dict = {
    'name': 'Alice',
    'age': 30,
    'birthday': datetime.now(),
    'favorite_numbers': np.array([1, 2, 3, 4, 5]),
    'balance': Decimal('123.45')
}

# Serialize the dictionary
serialized_dict = task_func(my_dict)

# Print the serialized dictionary
print(serialized_dict)