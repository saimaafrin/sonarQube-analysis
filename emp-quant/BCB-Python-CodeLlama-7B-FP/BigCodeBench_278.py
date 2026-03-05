import numpy as np
from sympy import symbols, solve
def task_func(precision=2, seed=0):
    """
    Solves a quadratic equation in the form of ax^2 + bx + c = 0, where a, b, and c are randomly generated numbers between -10 and 10.
    The solutions are complex numbers rounded to the specified accuracy.
    """
    # Generate random numbers between -10 and 10
    a = np.random.randint(-10, 10, size=1)[0]
    b = np.random.randint(-10, 10, size=1)[0]
    c = np.random.randint(-10, 10, size=1)[0]

    # Create symbols for the variables
    x = symbols('x')

    # Solve the equation
    solutions = solve(a*x**2 + b*x + c, x, dict=True)

    # Round the solutions to the specified precision
    solutions = [round(solution, precision) for solution in solutions]

    # Return the solutions as a tuple
    return tuple(solutions)