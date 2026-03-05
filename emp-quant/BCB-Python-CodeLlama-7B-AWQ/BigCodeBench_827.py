import math
from sympy import isprime
def task_func(input_list):
    """
    Filter the prime numbers from the specified list, sort the prime numbers ascending based on their radian value converted to degrees, and return the sorted list.
    The function uses the isprime function from the sympy library to determine prime numbers and the degrees function from the math library to sort the numbers based on their degree value.
    """
    # Filter the prime numbers from the input list
    prime_numbers = [x for x in input_list if isprime(x)]

    # Sort the prime numbers ascending based on their radian value converted to degrees
    sorted_prime_numbers = sorted(prime_numbers, key=lambda x: math.degrees(math.radians(x)))

    return sorted_prime_numbers
input_list = [101, 102, 103, 104]