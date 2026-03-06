
import math
from sympy import isprime

def task_func(input_list):
    # Filter out non-prime numbers
    primes = [num for num in input_list if isprime(num)]
    
    # Sort the prime numbers based on their degree value (radian to degree conversion)
    sorted_primes = sorted(primes, key=lambda x: math.degrees(math.atan(x)))
    
    return sorted_primes