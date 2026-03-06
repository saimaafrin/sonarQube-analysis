
import heapq
import random

class Object:
    def __init__(self, value):
        self.test = value

def task_func(obj_list, attr, top_n=5, seed=None):
    if not obj_list:
        return [], None

    # Set the random seed if provided
    if seed:
        random.seed(seed)

    # Create a list of tuples containing the attribute value and the object
    attr_list = [(getattr(obj, attr), obj) for obj in obj_list]

    # Sort the list by the attribute value in descending order
    sorted_list = sorted(attr_list, key=lambda x: x[0], reverse=True)

    # Get the top N values
    top_values = [obj[0] for obj in sorted_list[:top_n]]

    # Get a randomly chosen value of all attributes
    random_value = random.choice([obj[0] for obj in attr_list])

    return top_values, random_value