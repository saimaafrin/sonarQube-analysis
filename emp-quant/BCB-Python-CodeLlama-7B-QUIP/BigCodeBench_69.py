
import random
import matplotlib.pyplot as plt
# Constants
SALARY_RANGE = (20000, 100000)
def task_func(dict1):
    # Generate random salaries for each employee
    salaries = [random.randint(SALARY_RANGE[0], SALARY_RANGE[1]) for i in range(dict1['num_employees'])
    # Create a histogram
    fig, ax = plt.subplots()
    ax.hist(salaries, bins=50, label='Salary Distribution in EMPXX Department')
    ax.set_xlabel('Salary')
    ax.set_ylabel('Number of Employees')
    ax.set_title('Salary Distribution in EMPXX Department')
    return ax