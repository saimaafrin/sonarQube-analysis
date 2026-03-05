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
    if seed is not None:
        random.seed(seed)

    # Create a list of tuples containing the attribute values and their indices
    attr_values = [(getattr(obj, attr), i) for i, obj in enumerate(obj_list)]

    # Sort the list by the attribute values in descending order
    attr_values.sort(key=lambda x: x[0], reverse=True)

    # Get the top N values and their indices
    top_values = [x[0] for x in attr_values[:top_n]]
    top_indices = [x[1] for x in attr_values[:top_n]]

    # Get a randomly sampled value of all attributes
    random_index = random.choice(top_indices)
    random_value = getattr(obj_list[random_index], attr)

    return top_values, random_value
class Object:
    def __init__(self, value):
        self.test = value
obj_list = [Object(random.randint(1, 12)) for _ in range(13)]