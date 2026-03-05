
import math
from sympy import isprime

def task_func(input_list):
    # Filter prime numbers from the input list
    prime_numbers = [num for num in input_list if isprime(num)]
    
    # Sort the prime numbers based on their degree value
    sorted_primes = sorted(prime_numbers, key=lambda x: math.degrees(math.atan(x)))
    
    return sorted_primes