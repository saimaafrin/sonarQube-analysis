
import random
import matplotlib.pyplot as plt

# Constants
SALARY_RANGE = (20000, 100000)

def task_func(dict1):
    # Extract the number of employees in the department with code 'EMPXX'
    num_employees = dict1.get('EMPXX', 0)
    
    # Generate random salaries for each employee within the specified range
    salaries = [random.randint(SALARY_RANGE[0], SALARY_RANGE[1]) for _ in range(num_employees)]
    
    # Create a histogram of the salaries
    fig, ax = plt.subplots()
    ax.hist(salaries, bins=10, edgecolor='black')
    
    # Set the title and labels for the histogram
    ax.set_title('Salary Distribution in EMPXX Department')
    ax.set_xlabel('Salary')
    ax.set_ylabel('Number of Employees')
    
    return ax