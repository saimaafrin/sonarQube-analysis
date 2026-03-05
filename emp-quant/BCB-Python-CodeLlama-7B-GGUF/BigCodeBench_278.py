
import numpy as np
from sympy import symbols, solve

def task_func(precision=2, seed=0):
    # Generate random numbers between -10 and 10
    a = np.random.uniform(-10, 10, 1)[0]
    b = np.random.uniform(-10, 10, 1)[0]
    c = np.random.uniform(-10, 10, 1)[0]

    # Create symbols for the variables
    x = symbols('x')

    # Define the equation
    eq = a * x ** 2 + b * x + c

    # Solve the equation
    solutions = solve(eq, x, dict=True)

    # Round the solutions to the specified precision
    rounded_solutions = [round(solution, precision) for solution in solutions]

    # Return the tuple of solutions
    return tuple(rounded_solutions)