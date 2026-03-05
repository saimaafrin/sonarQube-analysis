import numpy as np
from sympy import symbols, solve
def task_func(precision=2, seed=0):
    np.random.seed(seed)
    a = np.random.randint(-10, 11)
    b = np.random.randint(-10, 11)
    c = np.random.randint(-10, 11)
    
    x = symbols('x')
    equation = a*x**2 + b*x + c
    solutions = solve(equation, x)
    
    rounded_solutions = tuple(round(sol.evalf(), precision) for sol in solutions)
    
    return rounded_solutions