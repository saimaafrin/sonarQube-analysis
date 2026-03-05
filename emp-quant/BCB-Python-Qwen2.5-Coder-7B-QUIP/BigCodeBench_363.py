
from multiprocessing import Pool
import math

def calculate_factorial(number: int) -> tuple:
    if not isinstance(number, int) or number < 0:
        raise ValueError("Input must be a non-negative integer")
    return number, math.factorial(number)

def task_func(numbers: list) -> dict:
    with Pool() as pool:
        results = pool.map(calculate_factorial, numbers)
    return dict(results)