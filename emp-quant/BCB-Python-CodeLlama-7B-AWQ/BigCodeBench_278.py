import numpy as np
from sympy import symbols, solve
def task_func(precision=2, seed=0):
    """
    Solves a quadratic equation in the form of ax^2 + bx + c = 0, where a, b, and c are randomly generated numbers between -10 and 10.
    The solutions are complex numbers rounded to the specified accuracy.
    """
    np.random.seed(seed)
    a = np.random.randint(-10, 10)
    b = np.random.randint(-10, 10)
    c = np.random.randint(-10, 10)
    x1, x2 = solve(a*x**2 + b*x + c, x, solve_type='real')
    return (x1.round(precision), x2.round(precision))