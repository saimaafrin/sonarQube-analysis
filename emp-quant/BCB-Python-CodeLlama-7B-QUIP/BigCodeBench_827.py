
import math
from sympy import isprime

def task_func(input_list):
    # Filter the prime numbers from the list
    prime_numbers = [x for x in input_list if isprime(x)]

    # Sort the prime numbers based on their degree value
    sorted_prime_numbers = sorted(prime_numbers, key=math.degrees)

    return sorted_prime_numbers