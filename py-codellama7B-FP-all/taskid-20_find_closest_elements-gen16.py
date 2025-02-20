from typing import List, Tuple

def find_closest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ From a supplied list of numbers (of length at least two) select and return two that are the closest to each
    other and return them in order (smaller number, larger number).
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.2])
    (2.0, 2.2)
    >>> find_closest_elements([1.0, 2.0, 3.0, 4.0, 5.0, 2.0])
    (2.0, 2.0)
    """


    if len(numbers) == 0:
        return ()

    # Initialise a list of tuples with the first number as the "low" number and the second number as the "high"
    # number, and set the distance between them to "inf"
    closest_pair = [(numbers[0], numbers[0]), float('inf')]

    # Loop through all numbers
    for i in range(len(numbers)):
        # Loop through all remaining numbers
        for j in range(i+1, len(numbers)):
            # Compute the distance between the current pair of numbers
            distance = abs(numbers[i] - numbers[j])

            # If the current distance is closer than the previously stored distance, update the closest pair
            if distance < closest_pair[1]:
                closest_pair = (numbers[i], numbers[j])

    return closest_pair
