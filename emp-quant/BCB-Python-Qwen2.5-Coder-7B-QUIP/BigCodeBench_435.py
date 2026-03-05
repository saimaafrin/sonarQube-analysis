
import pandas as pd
from random import randint

def task_func(name: str, age: int, code: str, salary: float, bio: str) -> pd.DataFrame:
    # Define a list of job titles
    job_titles = ['Engineer', 'Manager', 'Analyst', 'Developer', 'Tester']
    
    # Generate a random job title
    job_title = job_titles[randint(0, len(job_titles) - 1)]
    
    # Create a dictionary with the employee details
    employee_details = {
        'Name': name,
        'Age': age,
        'Code': code,
        'Salary': salary,
        'Bio': bio,
        'Job Title': job_title
    }
    
    # Create a DataFrame with the employee details
    data_df = pd.DataFrame([employee_details])
    
    return data_df