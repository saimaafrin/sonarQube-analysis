import heapq
import random
def task_func(obj_list, attr, top_n=5, seed=None):
    """
    Find the top N values of the specified attribute in a list of objects.
    Return the top N values as well as a randomly sampled value of all attributes.
    """
    if not obj_list:
        return [], None

    # Set the random seed if provided
    if seed:
        random.seed(seed)

    # Create a list of tuples containing the attribute values and their indices
    attr_values = [(getattr(obj, attr), i) for i, obj in enumerate(obj_list)]

    # Sort the list of tuples by the attribute values
    attr_values.sort(key=lambda x: x[0])

    # Get the top N values and their indices
    top_values = [x[0] for x in attr_values[:top_n]]

    # Get a randomly sampled value of all attributes
    random_value = random.choice(attr_values)

    return top_values, random_value
class Object:
    def __init__(self, value):
        self.test = value
obj_list = [Object(random.randint(1, 12)) for _ in range(13)]