import random
import matplotlib.pyplot as plt
SALARY_RANGE = (20000, 100000)
def task_func(dict1):
    # Generate random salaries for each employee
    salaries = [random.randint(SALARY_RANGE[0], SALARY_RANGE[1]) for _ in range(len(dict1))]

    # Create a histogram
    fig, ax = plt.subplots()
    ax.hist(salaries, bins=50, edgecolor='black', linewidth=1, color='skyblue')
    ax.set_title('Salary Distribution in EMPXX Department')
    ax.set_xlabel('Salary')
    ax.set_ylabel('Number of Employees')
    ax.set_xlim(SALARY_RANGE[0], SALARY_RANGE[1])
    ax.set_ylim(0, len(dict1))
    ax.grid(True)

    return ax