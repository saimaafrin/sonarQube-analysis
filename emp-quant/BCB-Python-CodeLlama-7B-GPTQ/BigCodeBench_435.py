import pandas as pd
from random import randint
def task_func(name: str, age: int, code: str, salary: float, bio: str) -> pd.DataFrame:
    """
    Generate a Pandas DataFrame of employees with their details based on the input provided.
    The function should output with:
        data_df (pd.DataFrame): dataframe with columns: 'Name', 'Age', 'Code', 'Salary', 'Bio', 'Job Title'.
        The 'Job Title' is randomly assigned from the predefined job titles:
        'Engineer', 'Manager', 'Analyst', 'Developer', 'Tester'.
    """
    # Create a list of predefined job titles
    job_titles = ['Engineer', 'Manager', 'Analyst', 'Developer', 'Tester']

    # Generate a random job title for each employee
    job_titles_random = [job_titles[randint(0, len(job_titles) - 1)] for _ in range(len(name))]

    # Create a dictionary of employee details
    employee_details = {
        'Name': name,
        'Age': age,
        'Code': code,
        'Salary': salary,
        'Bio': bio,
        'Job Title': job_titles_random
    }

    # Create a Pandas DataFrame from the dictionary
    data_df = pd.DataFrame(employee_details)

    return data_df
name = ['John', 'Jane', 'Bob']
age = [25, 30, 35]
code = ['A123', 'B456', 'C789']
salary = [50000, 60000, 70000]
bio = ['I like to play soccer', 'I enjoy hiking', 'I am a foodie']