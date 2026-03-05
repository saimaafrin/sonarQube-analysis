from multiprocessing import Pool
import math
def calculate_factorial(number: int) -> tuple:
    return number, math.factorial(number)
def task_func(numbers: list) -> dict:
    """
    Calculate factorials for a list of numbers in parallel using multiprocessing.
    Raises:
        ValueError: If any element in the input list is not an integer or is negative.
    Returns:
        dict[int, int]: A dictionary with numbers as keys and their factorial as values.
    """
    if not all(isinstance(x, int) and x >= 0 for x in numbers):
        raise ValueError("Input list must contain only positive integers.")

    with Pool() as pool:
        results = pool.map(calculate_factorial, numbers)

    return {x: y for x, y in results}