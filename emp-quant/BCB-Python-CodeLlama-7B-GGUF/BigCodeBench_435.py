
import pandas as pd
from random import randint

def task_func(name: str, age: int, code: str, salary: float, bio: str) -> pd.DataFrame:
    # Create a list of predefined job titles
    job_titles = ['Engineer', 'Manager', 'Analyst', 'Developer', 'Tester']

    # Generate a random job title for each employee
    job_title = job_titles[randint(0, len(job_titles) - 1)]

    # Create a dictionary with employee details
    employee_details = {
        'Name': name,
        'Age': age,
        'Code': code,
        'Salary': salary,
        'Bio': bio,
        'Job Title': job_title
    }

    # Create a Pandas DataFrame from the dictionary
    data_df = pd.DataFrame(employee_details, index=[0])

    return data_df

data_df = task_func(name, age, code, salary, bio)

print(data_df)