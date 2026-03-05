
import numpy as np
from sympy import symbols, solve

def task_func(precision=2, seed=0):
    a = np.random.uniform(-10, 10, seed=seed)
    b = np.random.uniform(-10, 10, seed=seed)
    c = np.random.uniform(-10, 10, seed=seed)
    x = symbols('x')
    eq = a * x ** 2 + b * x + c
    solutions = solve(eq, x, precision=precision)
    return (solutions[0].round(precision), solutions[1].round(precision))