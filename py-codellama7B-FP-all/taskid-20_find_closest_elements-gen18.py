from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """

    # sort the list in ascending order
    numbers.sort()

    # set the closest distance to zero
    closest_distance = 0.0

    # initialize two indexes for the closest pair of numbers
    smaller_index = 0
    larger_index = 1

    # iterate through the list
    for i in range(len(numbers) - 1):
        # compute the distance between the current number and the next number
        distance = abs(numbers[i] - numbers[i + 1])

        # if this distance is closer to zero than the current closest distance
        if distance < closest_distance:
            # reset the smaller and larger indexes
            smaller_index = i
            larger_index = i + 1

            # update the closest distance
            closest_distance = distance

    # return the closest pair of numbers in order
    return (numbers[smaller_index], numbers[larger_index])
