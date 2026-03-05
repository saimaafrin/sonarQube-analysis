from multiprocessing import Pool
import math
def calculate_factorial(number: int) -> tuple:
    """
    Calculate the factorial of a given integer.

    Args:
        number (int): The number to calculate the factorial for.

    Returns:
        tuple: A tuple containing the number and its factorial.

    Raises:
        ValueError: If the input is not an integer or is negative.
    """
    if not isinstance(number, int):
        raise ValueError("Input must be an integer.")
    if number < 0:
        raise ValueError("Input must be non-negative.")
    return number, math.factorial(number)
def task_func(numbers: list) -> dict:
    """
    Calculate the factorials of a list of numbers in parallel using multiprocessing.

    Args:
        numbers (list): The list of numbers to calculate the factorials for.

    Returns:
        dict: A dictionary with numbers as keys and their factorials as values.
    """
    with Pool() as pool:
        results = pool.map(calculate_factorial, numbers)
        return {result[0]: result[1] for result in results}