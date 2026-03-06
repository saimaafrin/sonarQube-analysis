
from multiprocessing import Pool
import math

def calculate_factorial(number: int) -> tuple:
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")
    return number, math.factorial(number)

def task_func(numbers: list) -> dict:
    results = {}
    with Pool() as pool:
        for result in pool.map(calculate_factorial, numbers):
            results[result[0]] = result[1]
    return results