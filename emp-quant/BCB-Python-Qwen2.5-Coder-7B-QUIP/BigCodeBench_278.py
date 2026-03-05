
import numpy as np
from sympy import symbols, solve

def task_func(precision=2, seed=0):
    # Set the seed for the random number generator
    np.random.seed(seed)
    
    # Generate random coefficients a, b, and c between -10 and 10
    a = np.random.randint(-10, 11)
    b = np.random.randint(-10, 11)
    c = np.random.randint(-10, 11)
    
    # Define the symbol for the variable
    x = symbols('x')
    
    # Define the quadratic equation
    equation = a*x**2 + b*x + c
    
    # Solve the quadratic equation
    solutions = solve(equation, x)
    
    # Round the solutions to the specified precision
    solutions = [round(sol, precision) for sol in solutions]
    
    # Return the solutions as a tuple
    return tuple(solutions)