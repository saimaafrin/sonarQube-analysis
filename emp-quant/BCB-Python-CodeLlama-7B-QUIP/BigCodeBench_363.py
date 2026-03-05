
from multiprocessing import Pool
import math

def calculate_factorial(number: int) -> tuple:
    return number, math.factorial(number)

def task_func(numbers: list) -> dict:
    with Pool(processes=4) as pool:
        results = pool.map(calculate_factorial, numbers)
    return dict(results)

def check_input(numbers: list) -> bool:
    for number in numbers:
        if not isinstance(number, int) or number < 0:
            raise ValueError("Invalid input")
    return True

def main():
    numbers = [1, 2, 3, 4, 5]
    if check_input(numbers):
        result = task_func(numbers)
        print(result)
    else:
        print("Invalid input")