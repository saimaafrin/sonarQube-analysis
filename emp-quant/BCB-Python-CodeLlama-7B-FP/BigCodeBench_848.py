import heapq
import random
def task_func(obj_list, attr, top_n=5, seed=None):
    """
    Find the top N values of the specified attribute in a list of objects.
    Return the top N values as well as a randomly sampled value of all attributes.
    """
    if not obj_list:
        return [], None

    # Initialize the heap with the first object
    heap = [(getattr(obj_list[0], attr), obj_list[0])]

    # Add the remaining objects to the heap
    for obj in obj_list[1:]:
        value = getattr(obj, attr)
        heapq.heappush(heap, (value, obj))

    # Get the top N values
    top_values = [obj[0] for obj in heapq.nlargest(top_n, heap)]

    # Get a randomly sampled value of all attributes
    if seed is not None:
        random.seed(seed)
    random_value = random.choice([getattr(obj, attr) for obj in obj_list])

    return top_values, random_value
obj_list = [Object(random.randint(1, 12)) for _ in range(13)]